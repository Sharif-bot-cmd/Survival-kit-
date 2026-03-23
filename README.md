# Android Freedom Survival Kit
## Complete Setup Guide for Google's 2026 Android Lockdown

### ⚠️ IMPORTANT DISCLAIMER
This guide is for **educational/survival purposes only**. You are responsible for your own device. Backup all data before proceeding. This setup uses **legitimate Android APIs** (Device Owner, ADB, etc.) and is **not** a hack or exploit.

---

## Table of Contents
1. [What This Is & Why You Need It](#what-this-is--why-you-need-it)
2. [Understanding the Threat](#understanding-the-threat)
3. [The Solution Overview](#the-solution-overview)
4. [Prerequisites](#prerequisites)
5. [Step 1: Factory Reset & Clean Setup](#step-1-factory-reset--clean-setup)
6. [Step 2: Device Owner Setup (Dhizuku)](#step-2-device-owner-setup-dhizuku)
7. [Step 3: ADB/Shell Privileges (Shizuku)](#step-3-adbshell-privileges-shizuku)
8. [Step 4: App Modification Framework (LSPatch)](#step-4-app-modification-framework-lspatch)
9. [Step 5: Essential Xposed Modules](#step-5-essential-xposed-modules)
10. [Step 6: System Debloating (Canta)](#step-6-system-debloating-canta)
11. [Step 7: File-Based Encryption (FBE)](#step-7-file-based-encryption-fbe)
12. [Step 8: Final Verification](#step-8-final-verification)
13. [Maintaining Your Freedom](#maintaining-your-freedom)
14. [Troubleshooting](#troubleshooting)
15. [Glossary](#glossary)

---

## What This Is & Why You Need It

### The Problem
In August 2025, Google announced that starting **September 2026**, Android will block installation of apps from developers who haven't:
- Paid a registration fee
- Submitted government ID
- Uploaded their private signing key
- Agreed to Google's terms

This kills:
- **Sideloading** (installing APKs directly)
- **Alternative app stores** (F-Droid, Aurora)
- **Modified apps** (ReVanced, modded games)
- **Indie developers** (can't afford registration)
- **Anonymous apps** (whistleblowers, political tools)
- **Your freedom** to control your own device

### The Solution
This guide shows you how to use **legitimate Android enterprise features** to maintain complete control over your device, bypassing Google's restrictions **without rooting** or unlocking your bootloader.

### Why This Works
- **Device Owner** is an official Android API for enterprise device management
- **ADB** is a required developer tool Google cannot remove
- **App modification** is your right as a device owner
- **Your setup** uses intended Android features, not exploits

---

## Understanding the Threat

### What Google's 2026 Lockdown Does
```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE 2026                    AFTER 2026                  │
├─────────────────────────────────────────────────────────────┤
│  ✓ Install any APK              ✗ Only verified apps       │
│  ✓ Use F-Droid                  ✗ Alternative stores       │
│  ✓ Modify apps                  ✗ Signature checks         │
│  ✓ Anonymous development        ✗ Government ID required   │
│  ✓ Share apps freely            ✗ Google approval needed   │
│  ✓ Your device, your rules      ✗ Google's device, rules   │
└─────────────────────────────────────────────────────────────┘
```

### What Google's "Advanced Flow" Really Means
Google claims there will be an "advanced flow" for experienced users. **Don't believe it.** 
- No specifics provided
- No timeline
- Likely requires developer registration anyway
- Probably geographic restrictions (not available in most countries)
- Can be revoked at any time

### Your Setup vs. Google's Promise
| Feature | Google's "Advanced Flow" | My Setup |
|---------|-------------------------|------------|
| Exists now? | "May eventually" | ✓ YES |
| Requires ID? | Likely | ✗ NO |
| Requires fees? | Likely | ✗ NO |
| Works offline? | Probably not | ✓ YES |
| Can be revoked? | Yes | ✗ NO |
| Works in many countries? | Probably not | ✓ YES |

---

## The Solution Overview

### Your Defense Matrix
```
                    GOOGLE'S 2026 ATTACKS
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ Boot-time     │  │ App Signature │  │ SSL Pinning   │
│ Verification  │  │ Checks        │  │ & Dependencies│
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│ FBE + Password│  │ Core Patch    │  │ TrustMeAlready│
│ (encryption)  │  │ (signature    │  │ + FakeGapps   │
│               │  │  bypass)      │  │ (SSL bypass)  │
└───────────────┘  └───────────────┘  └───────────────┘
                           │
                           ▼
              ┌───────────────────────┐
              │   DEVICE OWNER        │
              │   (Dhizuku)           │
              │   └── Controls all    │
              │       system policies │
              └───────────────────────┘
```

### Tools You'll Need

| Tool | Purpose | Where to Get |
|------|---------|--------------|
| **Dhizuku** | Device Owner activation | [GitHub](https://github.com/iamr0s/Dhizuku) |
| **Shizuku** | ADB/Shell privileges | [GitHub](https://github.com/RikkaApps/Shizuku) |
| **LSPatch** | No-root Xposed framework | [GitHub](https://github.com/LSPosed/LSPatch) |
| **Canta** | System app debloating | [F-Droid](https://f-droid.org/packages/io.github.samolego.canta/) |
| **Owndroid** | App component control | [GitHub](https://github.com/bintianqi/owndroid) |
| **Termux** | Terminal emulator | [F-Droid](https://f-droid.org/packages/com.termux/) |

### Xposed Modules (via LSPatch)

| Module | Purpose |
|--------|---------|
| **Core Patch** | Disables APK signature verification |
| **FakeGapps** | Mimics Google Play Services |
| **TrustMeAlready** | Bypasses SSL certificate pinning |
| **Bootloader Spoofer** | Hides bootloader modifications |

---

## Prerequisites

### Hardware Requirements
- Android device (tested on Oppo A3x/CPH2641, works on most)
- USB cable (data transfer capable)
- Computer with internet access (Windows/Mac/Linux)

### Software Requirements
- Android SDK Platform Tools (ADB)
- Python 3.6+ (for automation script)
- USB Debugging enabled on device

### Enable USB Debugging
1. Go to **Settings → About Phone**
2. Tap **Build Number** 7 times (developer mode enabled)
3. Go to **Settings → Developer Options**
4. Enable **USB Debugging**
5. Enable **OEM Unlocking** (if available)

### Install ADB
```bash
# Ubuntu/Debian
sudo apt install adb

# macOS
brew install android-platform-tools

# Windows
# Download from: https://developer.android.com/studio/releases/platform-tools
# Extract and add to PATH
```

### Verify ADB Works
```bash
adb devices
# Should show your device (may need to authorize on phone)
```

---

## Step 1: Factory Reset & Clean Setup

### Why Factory Reset?
- Removes any existing Google account associations
- Prevents Google from linking device to your identity
- Ensures clean slate for Device Owner activation
- Allows offline setup without Google tracking

### ⚠️ WARNING: THIS DELETES ALL DATA ⚠️
- Back up photos, contacts, documents
- Save important app data
- Remove SD card (optional but recommended)
- **THIS CANNOT BE UNDONE**

### Method 1: Automated (Recommended)
Use the provided Python script:
```bash
# Download the script (or create android_freedom.py)
python3 owner.py
```

The script will:
1. Wait for device connection
2. Factory reset via ADB
3. Wait for device to reboot
4. Install Dhizuku APK
5. Set Device Owner
6. Verify setup

### Method 2: Manual Factory Reset
```bash
# Via ADB (if device is connected)
adb shell "am broadcast -a android.intent.action.MASTER_CLEAR"

# Alternative
adb reboot recovery
# Then use volume buttons to select "Wipe data/factory reset"
```

### After Factory Reset - IMPORTANT!
When the device reboots to setup wizard:
1. **DO NOT** connect to Wi-Fi (skip if possible)
2. **DO NOT** sign in to Google account
3. **SKIP** all setup steps
4. **ENABLE** USB Debugging again (repeat the steps)
5. **DISABLE** automatic system updates

### Why Offline Setup Matters
```
With Google account:
├── Google knows your device
├── Device ID registered
├── Usage tracked
└── Verification can be enforced

Without Google account (offline):
├── Ghost device
├── No association
├── No tracking
└── Google can't enforce verification
```

---

## Step 2: Device Owner Setup (Dhizuku)

### What is Dhizuku?
Dhizuku is an app that uses Android's **Device Owner** API to give you the highest possible privileges without root. Device Owner is an official Android feature for enterprise device management.

### Why Device Owner is Powerful
```
Privilege Levels:
├── Hardware (TrustZone) - can't control
├── Kernel - can't control (locked bootloader)
├── System Services - can't control
├── DEVICE OWNER ← YOU ARE HERE
│   └── Can control: updates, apps, policies, encryption
├── System Apps (Google Play Services)
├── Normal Apps
└── User
```

### Installation
```bash
# Download Dhizuku APK
# From: https://github.com/iamr0s/Dhizuku/releases

# Install via ADB
adb install Dhizuku-*.apk

# Set as Device Owner
adb shell dpm set-device-owner com.rosan.dhizuku/.server.DhizukuDAReceiver
```

### Verify Device Owner
```bash
adb shell dumpsys device_policy | grep -A10 "Device Owner"
```

Expected output:
```
Device Owner:
  admin=ComponentInfo{com.rosan.dhizuku/com.rosan.dhizuku.server.DhizukuDAReceiver}
  package=com.rosan.dhizuku
  isOrganizationOwnedDevice=true
  User ID: 0
```

### What Device Owner Allows You To Do
- **Block system updates** - prevent Google from pushing lockdown
- **Disable any app** - including Google Play Services
- **Set encryption policies** - force password protection
- **Reset passwords** - regain access if locked out
- **Wipe device** - nuclear option if compromised
- **Control app installations** - allow or block any app

---

## Step 3: ADB/Shell Privileges (Shizuku)

### What is Shizuku?
Shizuku provides a way for apps to use system APIs with higher privileges. It works with ADB to give apps elevated access without root.

### Why You Need Shizuku
- Allows apps like Canta to disable system apps
- Enables LSPatch to communicate with the system
- Provides terminal access via Termux (RISH mode)
- Essential for debloating and modifications

### Installation
1. Download Shizuku from [GitHub](https://github.com/RikkaApps/Shizuku/releases)
2. Install via ADB:
   ```bash
   adb install Shizuku-*.apk
   ```
3. Enable Wireless Debugging in Developer Options
4. Open Shizuku and pair using the code
5. Start Shizuku service

### Alternative: ADB Mode (Simpler)
```bash
# Start Shizuku via ADB
adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh
```

### Verify Shizuku is Running
Open Shizuku app → Should show "Shizuku is running"

### Using RISH (Recoverable Interactive SHell)
In Termux, you can use RISH to run commands with ADB privileges:
```bash
# In Termux
rish
# Now you can run commands with elevated privileges
locksettings set-password --user 0 YourPassword123
```

---

## Step 4: App Modification Framework (LSPatch)

### What is LSPatch?
LSPatch is a **no-root** Xposed framework that allows you to modify apps by injecting code into them. Unlike rooted Xposed, LSPatch modifies the APK file itself.

### How LSPatch Works
```
Original App APK
        │
        ▼
LSPatch injects Xposed framework
        │
        ▼
Modified APK (new signature)
        │
        ▼
Install modified APK
        │
        ▼
Xposed modules load inside app
```

### Installation
1. Download LSPatch from [GitHub](https://github.com/LSPosed/LSPatch/releases)
2. Install via ADB:
   ```bash
   adb install LSPatch-*.apk
   ```
3. Open LSPatch and grant Shizuku permissions

### Patching Apps
1. In LSPatch, select "Patch from storage"
2. Choose the APK you want to modify
3. Select "Embed modules" mode
4. Choose which Xposed modules to embed
5. LSPatch creates a modified APK
6. Install the patched APK

### Important Notes
- Patched apps have different signatures than originals
- Cannot update via Google Play (must patch new versions)
- Some apps detect modification (use TrustMeAlready to bypass)
- Use Core Patch to allow installation alongside originals

---

## Step 5: Essential Xposed Modules

### Core Patch
**Purpose:** Disables APK signature verification

**Why you need it:**
- Allows installation of modified apps (LSPatch patched apps)
- Allows installing apps over originals
- Bypasses Google's signature checks

**Installation:**
1. Download from [GitHub](https://github.com/LSPosed/CorePatch)
2. Patch Core Patch itself with LSPatch (yes, patch the module!)
3. Install the patched Core Patch
4. Enable in LSPatch manager

### FakeGapps
**Purpose:** Mimics Google Play Services

**Why you need it:**
- Apps require Google Play Services for many functions
- You've disabled/removed real Play Services
- FakeGapps tricks apps into thinking Play Services exists

**Installation:**
1. Download from [GitHub](https://github.com/whew-inc/FakeGapps)
2. Patch with LSPatch
3. Install and enable

### TrustMeAlready
**Purpose:** Bypasses SSL certificate pinning

**Why you need it:**
- Many apps check certificates for security
- Modified apps may fail these checks
- TrustMeAlready tells apps "certificate is fine"

**Installation:**
1. Download from [GitHub](https://github.com/Xposed-Modules-Repo/mfsx.xposed.trustmealready)
2. Patch with LSPatch
3. Install and enable

### Bootloader Spoofer
**Purpose:** Hides bootloader modifications

**Why you need it:**
- Banking apps, Netflix, etc. check bootloader status
- Even though your bootloader is locked, modifications trigger warnings
- Spoofer tells apps "bootloader is locked"

**Installation:**
1. Download from [GitHub](https://github.com/Blays/BootloaderSpoofer)
2. Patch with LSPatch
3. Install and enable

### Sensor Disabler
**Purpose:** Disables specific sensors

**Why you need it:**
- Privacy: prevent apps from using proximity sensor, etc.
- Some sensors can track you even when you think they're off

**Installation:**
1. Download from [GitHub](https://github.com/MrChandler/DisableProx)
2. Patch with LSPatch
3. Install and enable

---

## Step 6: System Debloating (Canta)

### What is Canta?
Canta is a system app uninstaller/manager that works with Shizuku to remove preinstalled apps you don't want.

### Why Debloat?
```
Preinstalled Apps to Remove:
├── Google Play Store (app installer)
├── Oppo statistics (telemetry)
├── Qualcomm location (hardware tracking)
├── OTA update apps (prevent forced updates)
├── Engineering modes (potential backdoors)
└── Any app you don't use
```

### Installation
1. Download Canta from [F-Droid](https://f-droid.org/packages/io.github.samolego.canta/)
2. Install via ADB:
   ```bash
   adb install Canta-*.apk
   ```
3. Grant Shizuku permissions when prompted

### Critical Apps to Remove

| Package | Purpose | Remove? |
|---------|---------|--------|
| `com.google.android.gms` | Play Services | NO (keep at factory version)|
| `com.google.android.gsf` | Google Services | NO (may break login but keep it) |
| `com.oplus.statistics.rom` | Oppo telemetry | ✓ YES |
| `com.qualcomm.location` | Qualcomm tracking | ✓ YES |
| `com.oplus.engineermode` | Engineering backdoor | ✓ YES |
| `com.oplus.engineercamera` | Camera backdoor | ✓ YES |
| `com.oplus.location` | Oppo location | ✓ YES |
| `com.oppo.ota` | OTA updates | NO (you can only suspend it)|

- this depends on your devices because mine is oppo and it is recommended that you must make gms and gsf to factory version if possible.

### What to Keep
```
Keep:
├── Android System WebView
├── Phone/SMS/Contacts (system apps)
├── Settings
├── Launcher
├── Keyboard
└── Core system services
```

### Using Canta
1. Open Canta
2. Tap on app to see details
3. Tap "Uninstall" (not "Disable")
4. Confirm removal

### Important: Don't Remove These
```
DO NOT REMOVE:
├── android (system framework)
├── com.android.shell (ADB access)
├── com.android.systemui (UI)
└── com.android.packageinstaller (installer)
```

---

## Step 7: File-Based Encryption (FBE)

### What is FBE?
File-Based Encryption encrypts files with your password. When FBE is active, the system cannot access any data until you enter your password at boot.

### Why FBE is Critical
```
Without FBE:
Reboot → System loads → Google verification runs → Blocked

With FBE:
Reboot → "ENTER PASSWORD" → System cannot load → Google cannot verify
```

### Enabling FBE
```bash
# In Termux with rish, or via ADB:
adb shell locksettings set-password --user 0 YOUR_PASSWORD
```

### Enable "Require Power Off Password"
On Oppo/ColorOS:
1. Settings → Security → Screen Lock
2. Secure lock settings
3. Enable "Require password to turn off phone"

### Verify FBE is Active
```bash
adb shell getprop ro.crypto.state
# Should return: "encrypted"

adb shell getprop ro.crypto.type
# Should return: "file"
```

### Password Security
- **Use a strong password** (not just PIN)
- **Write it down** somewhere safe
- **No recovery options** (Google can't help)
- **Enter wrong too many times = factory reset**

---

## Step 8: Final Verification

### Check Device Owner
```bash
adb shell dumpsys device_policy | grep -A10 "Device Owner"
```
Should show `com.rosan.dhizuku`

### Check Shizuku Status
Open Shizuku app → "Shizuku is running"

### Check LSPatch
Open LSPatch → Should show patched apps and modules

### Check Modules Active
Open each patched app → Verify module functions

### Check Debloat
```bash
adb shell pm list packages | grep google
```
Should show minimal Google packages

### Check FBE
```bash
adb shell getprop ro.crypto.state
# Should be "encrypted"
```

### Test Sideloading
```bash
# Download any APK
adb install test.apk
# Should install successfully
```

---

## Maintaining Your Freedom

### Block OTA Updates
```bash
# Via ADB
adb shell pm disable com.oppo.ota
adb shell pm disable com.google.android.update

# Via Canta
# Remove OTA packages completely
```

### Monitor Google Play Services
If Play Services returns:
```bash
# Disable permanently
adb shell pm disable com.google.android.gms
```

### Keep Modules Updated
- Core Patch (new Android versions)
- LSPatch (framework updates)
- Xposed modules (bug fixes)

### Regular Backups
```bash
# Backup app list
adb shell pm list packages > apps.txt

# Backup important APKs
adb shell pm path com.example.app
adb pull /data/app/com.example.app-*.apk
```

### Avoid Factory Reset
Factory reset = lose Device Owner status. If you must reset, repeat the setup process.

---

## Troubleshooting

### "Device Owner already set"
```bash
# Remove existing Device Owner
adb shell dpm remove-active-admin com.rosan.dhizuku/.server.DhizukuDAReceiver

# Try again
adb shell dpm set-device-owner com.rosan.dhizuku/.server.DhizukuDAReceiver
```

### "Not allowed to set device owner"
- Must have just factory reset
- No Google account signed in
- No other accounts on device
- Try: `adb shell dpm set-device-owner --user 0 com.rosan.dhizuku/.server.DhizukuDAReceiver`

### Shizuku stops after reboot
- Always enable Wireless Debugging before reboot
- Or use ADB mode to restart (depends on version): `adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh`

### Patched app won't install
- Uninstall original app first
- Use Core Patch to allow installation
- Check if signature conflict

### App detects modification
- Enable Bootloader Spoofer
- Enable TrustMeAlready
- Check if app has additional protections

### Banking app not working
- Enable all modules in LSPatch
- Use Bootloader Spoofer
- Some banks use hardware attestation (cannot bypass)

### "Google Play Services required" error
- FakeGapps should handle this
- If not, install MicroG as alternative

---

## Glossary

| Term | Meaning |
|------|---------|
| **ADB** | Android Debug Bridge - tool for communicating with Android devices |
| **AOSP** | Android Open Source Project - the open source core of Android |
| **Device Owner** | Highest privilege level on Android (enterprise feature) |
| **FBE** | File-Based Encryption - encrypts files with user password |
| **FOSS** | Free and Open Source Software |
| **LSPatch** | No-root Xposed framework for app modification |
| **MDM** | Mobile Device Management - enterprise device control |
| **OTA** | Over-The-Air - system updates delivered wirelessly |
| **RISH** | Recoverable Interactive SHell - Shizuku's terminal feature |
| **Sideloading** | Installing apps from outside Google Play Store |
| **SSL Pinning** | Security feature that verifies app certificates |
| **TrustZone** | ARM's secure hardware environment |
| **Xposed** | Framework for modifying Android system and apps |

---

## Final Words

### What You've Accomplished
```
┌─────────────────────────────────────────────────────────────┐
│  YOUR DEVICE NOW:                                           │
│  ✓ Has Device Owner privileges (Google can't override)     │
│  ✓ Can install any APK (verified or not)                   │
│  ✓ Modified apps work (ReVanced, modded games)             │
│  ✓ Alternative stores work (F-Droid, Aurora)               │
│  ✓ Google Play Services is optional (FakeGapps)            │
│  ✓ Bootloader hidden (Netflix, banking work)               │
│  ✓ Encrypted (no boot-time verification)                   │
│  ✓ Debloated (no spyware, no updates)                      │
│  ✓ YOURS - not Google's                                    │
└─────────────────────────────────────────────────────────────┘
```

### When September 2026 Comes
```
Everyone else: "My phone won't install anything!"
You: "Everything works normally"

Everyone else: "Google blocked my apps!"
You: "I still have F-Droid, ReVanced, everything"

Everyone else: "I need to pay Google to develop!"
You: "I can still share apps with friends"

Everyone else: "My phone is a brick"
You: "My phone is still free"
```

### Spread the Word
- Share this guide
- Make videos showing your working phone
- Join the KeepAndroidOpen movement
- Help others who want to be free

### Remember
- **You own your device** - not Google
- **You control what runs** - not a corporation
- **Your freedom matters** - fight for it

---

## Resources

- **KeepAndroidOpen.org** - Campaign website
- **F-Droid** - Free and open source app store
- **GitHub** - Source code for all tools
- **XDA Developers** - Community support

## Legal & Transparency
This project maintains transparent legal documentation and has established official communication with GitHub Support (Ticket: 3932406).
