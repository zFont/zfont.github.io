# Why File Handler is Required?

Devices from **Xiaomi (MIUI, HyperOS)**, **Huawei**, **Honor**, **Tecno**, and **Infinix** use a Theme system that stores files inside the `Android/data` directory. Starting from Android 11, access to this directory is restricted for security reasons.

To apply custom fonts on these devices, zFont 3 needs permission to access the `Android/data` directory. This is where file handlers come in.

## Available File Handler Methods

zFont 3 supports different methods to access restricted directories:

| Method                              | Difficulty | Compatibility    | Recommended       |
|-------------------------------------|------------|------------------|-------------------|
| **[Legacy](legacy)**                | Easy       | Android ≤ 10     | Limited           |
| **[Storage Access Framework](saf)** | Easy       | Android 11-12    | Limited           |
| **[Shizuku](shizuku)**              | Medium     | All devices      | ✅ **Best Choice** |
| **[zFile](zfile)**                  | Easy       | Varies by device | Unreliable        |
| **[Root](root)**                    | Hard       | All devices      | Advanced users    |

## Quick Recommendations

### ✅ Recommended: Shizuku
- Works on **all devices** and Android versions
- Most reliable long-term solution
- Requires one-time setup with computer or wireless debugging
- Stays active until reboot
- **[View Setup Guide →](shizuku)**

### ⚠️ Alternative: Storage Access Framework
- Easy setup, no computer needed
- **Only** works reliably on Android 11-12
- Limited or no support on Android 13+
- **[View Setup Guide →](saf)**

### ❌ Not Recommended: zFile
- Unreliable and inconsistent
- May stop working after updates
- No way to predict compatibility
- Use only as last resort
- **[View Setup Guide →](zfile)**

### 🔓 Advanced: Root
- Most powerful access
- Requires technical expertise
- Not suitable for average users
- If rooted, use Shizuku instead
- **[View Setup Guide →](root)**

### 📱 Legacy (Android 10 and below)
- No special setup required
- Direct file access available
- **[View Guide →](legacy)**

## Need Help Choosing?

**If you're on Android 11+:** Use **Shizuku** (best option) or try **SAF** if you want something simpler.

**If you're on Android 10 or below:** Use **Legacy** method (no setup needed).

**If nothing else works:** Try **zFile** as a last resort, but expect inconsistent results.

**If you have root access:** You can use **Root**, but **Shizuku** is still recommended for better security.

::: tip Remember
Shizuku requires one-time setup but provides the best experience for applying custom fonts on theme-based devices.
:::