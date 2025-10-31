# Shizuku <Badge type="tip" text="Recommended" />

::: tip Recommended Method
Shizuku is the most reliable method and works on after Android 12+ devices. This is the best choice.
:::

### Requirements

* Shizuku app—[Play Store](https://play.google.com/store/apps/details?id=moe.shizuku.privileged.api) or [GitHub](https://github.com/RikkaApps/Shizuku/releases)
* [Developer Options enabled on your device.](#enable-developer-options) <Badge type="warning" text="Required" />
* One of these:
  * [Wi-Fi (Wireless Debugging)](#start-by-using-wi-fi)
  * [Computer + USB cable](#start-using-computer-adb)

## Enable Developer Options <Badge type="warning" text="Required" />

Follow the steps for your device:

::: details Huawei, Honor & Most Android devices
1. Open **Settings**
2. Go to **About phone**
3. Tap **Build number** 7 times
4. You'll see "You are now a developer"

![Enable Developer Options (Huawei & Honor)](/images/filehandler/shizuku/dev-honor.jpg)
:::

::: details Xiaomi, Redmi, POCO (MIUI)
1. Open **Settings**
2. Go to **My device**
3. Tap **MIUI Version** 7 times
4. You'll see "You are now a developer"

![Enable Developer Options on MIUI](/images/filehandler/shizuku/dev-miui.jpg)
:::

::: details Xiaomi, Redmi, POCO (HyperOS)
1. Open **Settings**
2. Go to **My device**
3. Tap **OS Version** 7 times
4. You'll see "You are now a developer"

![Enable Developer Options on HyperOS](/images/filehandler/shizuku/dev-hyperos.jpg)
:::

::: details TECNO, Infinix
1. Open **Settings**
2. Go to **My phone**
3. Tap **Build number** 7 times
4. You'll see "You are now a developer"

![Enable Developer Options on HyperOS](/images/filehandler/shizuku/dev-tecnox.jpg)
:::

## Start by using Wi-Fi <Badge type="tip" text="Wireless Debugging" />
::: warning Requirements
- Android 11 or newer
- Wi-Fi connection required (can use mobile hotspot from another device)
:::
### Step 1: Allow Notification permission
1. Open **Shizuku** app 
2. Allow all necessary permissions when asked
3. Tap on **Pairing** button
4. Enable **Show notifications** toggle

![Allow Notification permission](/images/filehandler/shizuku/shizuku-noti.jpg)

### Step 2: Enable Wireless Debugging
1. Tap on **Developer options**
2. Scroll down and enable **USB debugging**
3. Find **Wireless debugging** and enable it.

![Enable Wireless debugging](/images/filehandler/shizuku/shizuku-debugging.jpg)

### Step 3: Pair device with pairing code
A notification will appear with a pairing prompt.
1. Enter the pairing code shown in the notification
2. Tap Pair

![Pair device with pairing code in notification popup](/images/filehandler/shizuku/shizuku-pairing.jpg)

::: details Didn't see the notification Popup?
If the notification popup doesn't appear:
1. Swipe down the notification panel
2. Look for Shizuku notification
3. Tap on **Enter pairing code**

![Pair device with pairing code inside Notification](/images/filehandler/shizuku/shizuku-pairing-noti.jpg)
:::

### Step 4: Start Shizuku
1. Go back to the **Shizuku** app
2. Tap on **Start** button

![Start Shizuku](/images/filehandler/shizuku/shizuku-start.jpg)

::: tip ✅ Ready!
When you see "**Shizuku is running**", you're all set!
Now you can use Shizuku in **zFont 3** → **Settings** → **File Handler**.
:::

## Start Using Computer (ADB)

For detailed instructions on using ADB with a computer, refer to the [Official Shizuku Guide](https://shizuku.rikka.app/guide/setup/#start-by-connecting-to-a-computer).

::: tip Use Another Android Phone as Computer
You can use another Android phone instead of a computer!

Install one of these apps on the second phone:
- [Bugjaeger](https://play.google.com/store/apps/details?id=eu.sisik.hackendebug)
- [ADB OTG](https://play.google.com/store/apps/details?id=com.htetznaing.adbotg)

Connect both phones with an OTG cable and follow the ADB instructions.
:::

## Using Shizuku with zFont 3
Once Shizuku is running:
1. Open **zFont 3**
2. Go to **Settings** → **File Handler**
3. Select **Shizuku**
4. Grant permission when prompted
5. Done! You can now apply fonts
6. 
## Troubleshooting & FAQ

### Shizuku won't start after successful pairing

**Solution:**
1. Go to **Settings** → **Developer options**
2. Toggle **Wireless debugging** off, then on again
3. Return to Shizuku app and tap **Start**

### Other issues?

For more troubleshooting and frequently asked questions, check the [Official Shizuku FAQ](https://shizuku.rikka.app/guide/setup/#faq).