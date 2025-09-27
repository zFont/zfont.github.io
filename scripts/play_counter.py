import csv
import json
import os
import sys
from datetime import datetime
from google.cloud import storage
from google.oauth2 import service_account
import base64


def get_credentials_from_base64(base64_string):
    """Create credentials from Base64 string (for GitHub secrets)."""
    json_string = base64.b64decode(base64_string).decode()
    import json
    credentials_dict = json.loads(json_string)
    return service_account.Credentials.from_service_account_info(credentials_dict)


def generate_month_year_pairs(start_date_str):
    """Generate month-year pairs from start date to current date."""
    start_date = datetime.strptime(start_date_str, '%Y-%m')
    current_date = datetime.now()
    pairs = []

    while start_date <= current_date:
        pairs.append((start_date.month, start_date.year))
        if start_date.month == 12:
            start_date = start_date.replace(year=start_date.year + 1, month=1)
        else:
            start_date = start_date.replace(month=start_date.month + 1)

    return pairs


def format_number_short(num):
    suffixes = ['', 'K', 'M', 'B', 'T']
    suffix = suffixes[0]
    for suffix in suffixes:
        if num < 1000:
            break
        if suffix != 'T':  # Don't divide if we're at the last suffix
            num /= 1000

    # Format: no decimals for integers, clean decimals otherwise
    if num == int(num):
        return f"{int(num)}{suffix}"
    return f"{num:.1f}{suffix}".rstrip('0').rstrip('.')


def parse_csv_line(line):
    """Parse CSV line to extract download count."""
    try:
        line_data = list(csv.reader([line]))[0]
        if len(line_data) >= 3:
            return int(line_data[-3])  # Third from last column
    except (ValueError, IndexError):
        pass
    return 0


def get_monthly_downloads(client, bucket_name, app_package_name, month, year):
    """Get download count for a specific month."""
    file_name = f'installs_{app_package_name}_{year}{month:02}_overview.csv'
    file_path = f'stats/installs/{file_name}'

    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(file_path)

        if not blob.exists():
            return 0

        monthly_downloads = 0
        with blob.open("r", encoding='utf-16le') as f:
            next(f, None)  # Skip header
            for line in f:
                monthly_downloads += parse_csv_line(line)

        return monthly_downloads
    except Exception:
        return 0


def main():
    # Get environment variables
    bucket_name = os.getenv('BUCKET_NAME')
    service_account = os.getenv('SERVICE_ACCOUNT')
    app_package_name = os.getenv('APP_PACKAGE_NAME')
    start_date = os.getenv('START_DATE')
    output_path = os.getenv('OUTPUT_PATH', 'play-report.json')

    # Validate required environment variables
    required_vars = {
        'BUCKET_NAME': bucket_name,
        'SERVICE_ACCOUNT': service_account,
        'APP_PACKAGE_NAME': app_package_name,
        'START_DATE': start_date
    }

    missing_vars = [var for var, value in required_vars.items() if not value]
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)

    try:
        # Initialize Google Cloud Storage client
        credentials = get_credentials_from_base64(service_account)
        client = storage.Client(credentials=credentials)

        # Generate month-year pairs
        month_year_pairs = generate_month_year_pairs(start_date)

        # Calculate total downloads
        total_downloads = 0
        monthly_data = {}

        print(f"Processing {len(month_year_pairs)} months of data...")

        for month, year in month_year_pairs:
            monthly_downloads = get_monthly_downloads(client, bucket_name, app_package_name, month, year)
            total_downloads += monthly_downloads
            monthly_data[f"{year}-{month:02d}"] = monthly_downloads
            print(f"{year}-{month:02d}: {monthly_downloads:,} downloads")

        # Calculate yearly totals and find peak month
        yearly_totals = {}
        peak_month = {"downloads": 0}

        for month_year, downloads in monthly_data.items():
            year = month_year.split('-')[0]
            yearly_totals[year] = yearly_totals.get(year, 0) + downloads

            if downloads > peak_month["downloads"]:
                peak_month = {
                    "month": month_year,
                    "downloads": downloads,
                    "formatted_downloads": f"{downloads:,}"
                }

        # Create report with summary
        report = {
            "package_name": app_package_name,
            "total_downloads": total_downloads,
            "total_downloads_formatted": f"{total_downloads:,}",
            "total_downloads_summary": format_number_short(total_downloads),
            "report_generated_at": datetime.now().isoformat(),
            "data_period": {
                "start": start_date,
                "end": datetime.now().strftime('%Y-%m')
            },
            "summary": {
                "total_years": len(yearly_totals),
                "total_months": len(month_year_pairs),
                "average_downloads_per_month": round(
                    total_downloads / len(month_year_pairs)) if month_year_pairs else 0,
                "average_downloads_per_month_formatted": f"{round(total_downloads / len(month_year_pairs)):,}" if month_year_pairs else "0",
                "peak_month": peak_month,
                "yearly_totals": yearly_totals,
                "yearly_totals_formatted": {year: f"{total:,}" for year, total in yearly_totals.items()}
            },
            "monthly_data": monthly_data
        }

        # Save report
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\nTotal Downloads: {total_downloads:,}")
        print(f"Average per month: {report['summary']['average_downloads_per_month']:,}")
        print(f"Peak month: {peak_month['month']} with {peak_month['downloads']:,} downloads")
        print(f"\nYearly breakdown:")
        for year, total in yearly_totals.items():
            print(f"  {year}: {total:,} downloads")
        print(f"Report saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()