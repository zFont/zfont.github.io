### Storage Access Framework (SAF) <Badge type="warning" text="Android 11-12" />

::: warning Limited Compatibility
SAF works best on **Android 11-12**. Limited or no support on Android 13+.
:::

## What is SAF?

Storage Access Framework (SAF) is Android's built-in system for granting apps access to specific folders. It's the easiest method to set up but has compatibility limitations on newer Android versions.

## Compatibility

| Android Version | Status                        |
|-----------------|-------------------------------|
| Android 11      | ✅ Works well                  |
| Android 12      | ✅ Works well                  |
| Android 13+     | ⚠️ Limited (device-dependent) |

## Setup Steps

### Step 1: Go to File Handler Settings
1. Open **zFont 3** app
2. Go to **Settings** → **File Handler**
3. Select **Storage Access Framework**
4. Tap **Get Started**

![Settings > File Handler](/images/filehandler/saf/saf-select.jpg)

::: details SAF Unsupported?
If you see the "SAF Unsupported" message, your device may not support SAF.

We recommend using **[Shizuku](shizuku.html)** method instead.

If you want to try anyway:
1. Tap **Ignore**
2. Check **Use bypass**
3. Click **Get Started**

![Ignore SAF Unsupported](/images/filehandler/saf/saf-ignore.jpg)
:::

### Step 2: Grant Access
1. You'll be redirected to your device's theme directory
2. Tap **Use this folder** at the bottom

![SAF Allow](/images/filehandler/saf/saf-allow.jpg)

### Step 3: Done!
When **File Handler** status shows **Storage Access Framework**, you're ready!

![SAF Ready](/images/filehandler/saf/saf-ready.jpg)

✅ **Setup Complete!** You can now apply custom fonts.

## Troubleshooting

### Can't use this folder

**Solutions:**
1. Try toggling the **Use bypass** option (check/uncheck)
2. Use **[Shizuku](shizuku.html)** method instead (recommended)

### SAF stops working after update

**Solution:** Re-grant permission or switch to **[Shizuku](shizuku.html)** for better reliability.

## Limitations

::: danger Known Issues
- **Android 13+:** Many devices block SAF access
- **Manufacturer restrictions:** Some brands prevent SAF usage
- **Updates may reset permissions**
- **Inconsistent behavior** across different devices
  :::

**Why?** Google restricted `Android/data` access starting from Android 11 for security. From Android 13, even SAF access is being limited on many devices.

## When to Use SAF

✅ **Use SAF if:**
- You're on Android 11 or 12
- You want the simplest setup
- No access to a computer

❌ **Use Shizuku instead if:**
- You're on Android 13+
- You need long-term reliability
- SAF doesn't work on your device

## Alternative Methods

- **[Shizuku](shizuku.html)** - Most reliable, works on all versions
- **[zFile](zfile.html)** - Unreliable fallback option
- **[Root](root.html)** - For advanced users