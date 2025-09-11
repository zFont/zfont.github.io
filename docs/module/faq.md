### Systemless Module Guide <Badge type="danger" text="Advanced" />

zFont 3 supports creating systemless font modules for advanced users to flash through [Magisk](https://github.com/topjohnwu/Magisk), [KernelSU](https://kernelsu.org/), or [APatch](https://apatch.dev/). Since some Android manufacturers restrict custom font changes, you can use this method to change any font and emoji on Android devices. This method will change all system fonts across every app.

::: warning Important
This guide is for **Advanced users** only. If you are not familiar with ROOT, we do not recommend using this method.

**Important considerations:**
- ROOT will void your device warranty
- Always **backup your data** before proceeding
- Ensure you understand the risks involved
  :::

## Create Emoji Module

Creating an emoji module is straightforward:

1. Click the **Create Module** button
2. zFont 3 automatically handles all module creation steps
3. No additional configuration required

## Create Font Module

Font module creation depends on your target language and requires proper font mapping.

### Basic Font Mapping

For **English fonts**, map your custom fonts to the corresponding system fonts:

| Your Font File | Maps To System Font |
|---|---|
| MyFont-Regular.ttf | → Roboto-Regular.ttf |
| MyFont-Bold.ttf | → Roboto-Bold.ttf |
| MyFont-BoldItalic.ttf | → Roboto-BoldItalic.ttf |
| MyFont-Italic.ttf | → Roboto-Italic.ttf |

::: warning Important
Mapping only `Roboto-Regular.ttf` will **not** change fonts system-wide. You must include all font styles (Bold, Italic, BoldItalic) for complete font replacement.
:::

### Language-Specific Fonts

For **non-English languages**, use the appropriate system font family:

- **Myanmar**: Use `NotoSans-Myanmar` family
    - Replace `-Regular.ttf` with your Regular variant
    - Replace `-Bold.ttf` with your Bold variant
- **Other languages**: Check your system's font directory for the correct font family name

### Font Mapping Examples

**Complete English Font Set:**
```
MyCustomFont-Regular.ttf → Roboto-Regular.ttf
MyCustomFont-Bold.ttf → Roboto-Bold.ttf  
MyCustomFont-Italic.ttf → Roboto-Italic.ttf
MyCustomFont-BoldItalic.ttf → Roboto-BoldItalic.ttf
```

**Myanmar Font Set:**
```
MyMyanmarFont-Regular.ttf → NotoSans-Myanmar-Regular.ttf
MyMyanmarFont-Bold.ttf → NotoSans-Myanmar-Bold.ttf
```

## Installation Process

### Method 1: Direct Flash (Basic)
1. After creating your module, click **Flash** in the dialog
2. zFont 3 will install the module directly

### Method 2: Module Manager (Recommended)
1. Create your module in zFont 3
2. Open your root solution manager:
    - **Magisk Manager**
    - **KernelSU Manager**
    - **APatch Manager**
3. Install the module through the manager
4. **Reboot your device** to apply changes

::: tip Recommendation
Using a module manager provides better control and easier management of your font modules.
:::

## Post-Installation

After installation and reboot:
- Check if fonts display correctly across all apps
- Verify all font weights (Regular, Bold, Italic) work properly
- If issues occur, ensure all required font variants were mapped correctly