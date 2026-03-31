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
   - [5.1 Core Patch](#core-patch)
   - [5.2 FakeGapps](#fakegapps)
   - [5.3 TrustMeAlready](#trustmealready)
   - [5.4 Bootloader Spoofer](#bootloader-spoofer)
   - [5.5 NoVPNDetect](#novpndetect)
   - [5.6 Sensor Disabler](#sensor-disabler)
   - [5.7 FuckGoogleLicense](#fuckgooglelicense)
   - [5.8 DAX (Dhizuku API for Xposed)](#dax-dhizuku-api-for-xposed)
10. [Step 6: System Debloating (Canta)](#step-6-system-debloating-canta)
11. [Step 7: File-Based Encryption (FBE)](#step-7-file-based-encryption-fbe)
12. [Step 8: Enable Common Criteria Mode](#step-8-enable-common-criteria-mode)
13. [Step 9: Cellular Security (Sentry Radio)](#step-9-cellular-security-sentry-radio)
14. [Step 10: Network Lockdown (Owndroid + Rethink DNS)](#step-10-network-lockdown-owndroid--rethink-dns)
15. [Step 11: Final Verification](#step-11-final-verification)
16. [Maintaining Your Freedom](#maintaining-your-freedom)
17. [Troubleshooting](#troubleshooting)
18. [Proof: Dumpsys Output](#proof-dumpsys-output)
19. [Glossary](#glossary)

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
| **Owndroid** | App component control, VPN lockdown | [GitHub](https://github.com/bintianqi/owndroid) |
| **Termux** | Terminal emulator | [F-Droid](https://f-droid.org/packages/com.termux/) |
| **Rethink DNS** | Firewall + VPN with lockdown mode | [F-Droid](https://f-droid.org/packages/com.celzero.bravedns/) |
| **Sentry Radio** | Cellular security, IMSI catcher detection | [GitHub](https://github.com/fzer0x/imsicatcher-detector) |

### Xposed Modules (via LSPatch)

| Module | Purpose |
|--------|---------|
| **Core Patch** | Disables APK signature verification |
| **FakeGapps** | Mimics Google Play Services (critical for hybrid setup) |
| **TrustMeAlready** | Bypasses SSL certificate pinning |
| **Bootloader Spoofer** | Hides bootloader modifications |
| **NoVPNDetect** | Prevents apps from detecting VPN usage |
| **Sensor Disabler** | Disables specific sensors for privacy |
| **FuckGoogleLicense** | Bypasses Google Service License Verification |
| **DAX** | Dhizuku API for Xposed (grants Device Owner privileges to modules) |

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

### Critical Understanding: Self-Patching vs. Embedding

| Method | How It Works | Scope |
|--------|--------------|-------|
| **Self-patch module** | Patch the module APK itself with LSPatch | Module runs independently, can hook system-wide via Shizuku |
| **Embed module into target app** | Embed module into a specific app | Module ONLY affects that one app |

**For system-wide effect, ALWAYS self-patch your modules.** LSPatch needs Shizuku service activated for system-wide hooks.

### Installation
1. Download LSPatch from [GitHub](https://github.com/LSPosed/LSPatch/releases)
2. Install via ADB:
   ```bash
   adb install LSPatch-*.apk
   ```
3. Open LSPatch and grant Shizuku permissions

### Patching Apps (Self-Patch Method)
1. In LSPatch, select "Patch from storage"
2. Choose the module APK you want to patch
3. Select "Embed modules" mode
4. Choose which modules to embed (for DAX, embed it into other modules)
5. LSPatch creates a modified APK
6. Install the patched module

### Important Notes
- Patched apps have different signatures than originals
- Cannot update via Google Play (must patch new versions)
- Some apps detect modification (use TrustMeAlready to bypass)
- Use Core Patch to allow installation alongside originals
- **"System service not running" warning is normal** - modules work via Shizuku

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
2. **Self-patch** Core Patch with LSPatch
3. Install the patched Core Patch
4. Enable in LSPatch manager

---

### FakeGapps
**Purpose:** Mimics Google Play Services

**Why you need it:**
- Apps require Google Play Services for many functions
- You're keeping Play Services at **factory version** (not updated)
- FakeGapps tricks apps into thinking Play Services is current

**The Hybrid Approach (Critical):**
```
Apps request: "I need Play Services v25.0"
         ↓
FakeGapps intercepts: "I'm v25.0" (lies)
         ↓
Factory Play Services (v15.0) provides actual functionality
         ↓
App runs happily, never knows the difference
```

**Installation:**
1. Download from [GitHub](https://github.com/whew-inc/FakeGapps)
2. **Self-patch** FakeGapps with LSPatch
3. Install and enable

---

### TrustMeAlready
**Purpose:** Bypasses SSL certificate pinning

**Why you need it:**
- Many apps check certificates for security
- Modified apps may fail these checks
- TrustMeAlready tells apps "certificate is fine"

**Installation:**
1. Download from [GitHub](https://github.com/Xposed-Modules-Repo/mfsx.xposed.trustmealready)
2. **Self-patch** TrustMeAlready with LSPatch
3. Install and enable

---

### Bootloader Spoofer
**Purpose:** Hides bootloader modifications

**Why you need it:**
- Banking apps, Netflix, etc. check bootloader status
- Even though your bootloader is locked, modifications trigger warnings
- Spoofer tells apps "bootloader is locked"

**Installation:**
1. Download from [GitHub](https://github.com/Xposed-Modules-Repo/es.chiteroman.bootloaderspoofer)
2. **Self-patch** Bootloader Spoofer with LSPatch
3. Install and enable

---

### NoVPNDetect
**Purpose:** Prevents apps from detecting VPN usage

**Why you need it:**
- You'll be using VPN lockdown to block Google verification servers
- Many apps refuse to work when VPN is detected
- This module tells apps "no VPN is active"

**Installation:**
1. Download from [GitHub](https://github.com/Xposed-Modules-Repo/me.hoshino.novpndetect)
2. **Self-patch** NoVPNDetect with LSPatch
3. Install and enable

---

### Sensor Disabler
**Purpose:** Disables specific sensors

**Why you need it:**
- Privacy: prevent apps from using proximity sensor, etc.
- Some sensors can track you even when you think they're off

**Installation:**
1. Download from [GitHub](https://github.com/MrChandler/DisableProx)
2. **Self-patch** Sensor Disabler with LSPatch
3. Install and enable

---

### FuckGoogleLicense
**Purpose:** Bypasses Google Service License Verification

**Why you need it:**
- Many apps check with Google Play Licensing Library
- Google could revoke licenses for "unverified" apps in 2026
- This module intercepts license checks and returns "LICENSED"

**Installation:**
1. Download from [GitHub](https://github.com/jiguro/FuckGoogleLicense)
2. **Self-patch** FuckGoogleLicense with LSPatch
3. Install and enable

---

### DAX (Dhizuku API for Xposed)
**Purpose:** Grants Device Owner privileges to Xposed modules

**What DAX Does:**
- Acts as a bridge between Xposed modules and Dhizuku
- Allows modules to access Device Owner APIs
- Critical for modules that need system-level authority

**Why You Need DAX:**
| Without DAX | With DAX |
|-------------|----------|
| Modules run with Shizuku privileges (UID 2000) | Modules gain Device Owner privileges |
| Can't access Device Owner APIs | Full Device Owner access |
| Limited to ADB-level operations | Can perform policy enforcement, wipe, lock |

**Installation (Critical - DO NOT self-patch DAX):**
1. Download DAX from [Dhizuku releases](https://github.com/iamr0s/Dhizuku-API-Xposed)
2. **DO NOT self-patch DAX** - it's designed to be embedded
3. When patching other modules (Core Patch, FakeGapps, etc.), **embed DAX into them**
4. In LSPatch, select the module APK → "Embed modules" → choose DAX
5. Install the patched module with DAX embedded

**Which Modules Should Have DAX Embedded:**
| Module | Embed DAX? | Why |
|--------|------------|-----|
| Core Patch | ✅ Yes | Signature bypass with Device Owner authority |
| FakeGapps | ✅ Yes | Play Services spoofing at system policy level |
| Bootloader Spoofer | ✅ Yes | Hide from Play Integrity API |
| FuckGoogleLicense | ✅ Yes | License bypass at policy level |
| TrustMeAlready | ⚠️ Optional | Works without, but can benefit |
| NoVPNDetect | ⚠️ Optional | VPN bypass doesn't strictly need it |

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

### Critical Apps to Handle

| Package | Purpose | Action |
|---------|---------|--------|
| `com.google.android.gms` | Play Services | **KEEP at factory version** - Do NOT remove or update |
| `com.google.android.gsf` | Google Services | **KEEP** - Keep for compatibility |
| `com.oplus.statistics.rom` | Oppo telemetry | ✓ REMOVE |
| `com.qualcomm.location` | Qualcomm tracking | ✓ REMOVE |
| `com.qti.qcc` | Qualcomm telemetry | ✓ REMOVE |
| `com.oplus.engineermode` | Engineering backdoor | ✓ REMOVE |
| `com.oplus.engineercamera` | Camera backdoor | ✓ REMOVE |
| `com.oplus.location` | Oppo location | ✓ REMOVE |
| `com.oplus.locationproxy` | Location proxy | ✓ REMOVE |
| `com.qualcomm.qti.devicestatisticsservice` | Device stats | ✓ REMOVE |
| `com.oppo.ota` | OTA updates | SUSPEND (do not remove) |

> **Important:** The hybrid approach requires keeping Play Services at its factory version. The lockdown code does NOT exist in factory Play Services. FakeGapps then spoofs version checks so apps think it's current.

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

## Step 8: Enable Common Criteria Mode

### What is Common Criteria Mode?
Common Criteria is a global security standard for government and enterprise devices. When enabled:
- Strict SELinux policies are enforced
- Kernel-level restrictions on app interactions
- No unauthorized debugging
- System integrity checks at boot

### Why This Matters
Common Criteria Mode is a **legitimate enterprise security feature** that:
- Cannot be disabled by Google Play Services
- Makes your device appear as a government-grade secure device
- Blocks privilege escalation attempts
- Prevents forced OTA updates

### Enabling via Owndroid
1. Install Owndroid from [GitHub](https://github.com/bintianqi/owndroid)
2. Grant Dhizuku permissions
3. Navigate to security settings
4. Enable **Common Criteria Mode**

### Verify Common Criteria Mode
```bash
adb shell dumpsys device_policy | grep mCommonCriteriaMode
```
Expected output:
```
mCommonCriteriaMode=true
```

---

## Step 9: Cellular Security (Sentry Radio)

### What is Sentry Radio?
Sentry Radio (formerly IMSICatcher Detector) detects and blocks:
- Fake cell towers (IMSI catchers / Stingrays)
- Cellular surveillance attempts
- Forced downgrade attacks (2G/3G)
- Silent SMS tracking
- Baseband exploitation

### Critical Settings to Enable (Even Without Root)

| Setting | Purpose | Works Without Root? |
|---------|---------|---------------------|
| **Automatic Threat Mitigation** | Instantly responds to detected threats | ✅ Yes (via Xposed) |
| **Block GSM Registrations** | Prevents 2G connection (vulnerable network) | ✅ Yes (via Xposed) |
| **Reject A5/0 Cipher** | Blocks unencrypted cellular connections | ✅ Yes (via Xposed) |
| **Mark Fake Cells** | Blacklists suspicious towers | ✅ Yes (via Xposed) |
| **Force Immediate LTE** | Stays on secure 4G/5G networks | ✅ Yes (via Xposed) |

### Why Xposed Is Sufficient
Even without root, Xposed hooks into Android's telephony framework at the RIL (Radio Interface Layer) level. Your modules can:
- Intercept network registration requests
- Reject weak encryption ciphers
- Block 2G connections entirely
- Identify and blacklist fake towers

### Installation
1. Download Sentry Radio from [GitHub](https://github.com/fzer0x/SentryRadio/releases)
2. Install via ADB:
   ```bash
   adb install SentryRadio-*.apk
   ```
3. Open Sentry Radio and enable all protection settings
4. Grant Shizuku permissions if prompted

### Verify Cellular Protection
```bash
adb shell dumpsys telephony.registry | grep "RegState"
# Expected: POWER_OFF (radio disabled for protection)
```

---

## Step 10: Network Lockdown (Owndroid + Rethink DNS)

### Why Network Lockdown Is Critical
Google's lockdown enforcement requires network connectivity. By controlling your network at the Device Owner level, you block:
- Play Services updates
- Developer verification queries
- Remote policy changes
- Carrier OTA pushes

### The Two-Layer Approach

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: Owndroid (Device Owner)                          │
│  └── "Lockdown admin configured network"                   │
│  └── Enforces VPN at system level                          │
│  └── Cannot be bypassed by ANY app                         │
├─────────────────────────────────────────────────────────────┤
│  LAYER 2: Rethink DNS (VPN Service)                        │
│  └── Always-on VPN lockdown enabled                        │
│  └── Firewall rules active                                 │
│  └── Google verification servers blocked                   │
└─────────────────────────────────────────────────────────────┘
```

### Step 10.1: Configure Owndroid VPN Lockdown

1. Open **Owndroid**
2. Grant Dhizuku permissions
3. Navigate to **Network / VPN settings**
4. Enable **"Lockdown admin configured network"**
5. Set Rethink DNS as the always-on VPN

### Step 10.2: Configure Rethink DNS

1. Install Rethink DNS from [F-Droid](https://f-droid.org/packages/com.celzero.bravedns/)
2. Open Rethink DNS
3. Enable **Always-on VPN**
4. Enable **Lockdown mode** (blocks all traffic if VPN fails)
5. Add firewall rules to block Google domains:
   - `*.google.com/verification`
   - `android.clients.google.com`
   - `play.googleapis.com`
   - `*.googleapis.com`

### Verify VPN Lockdown
```bash
adb shell dumpsys device_policy | grep -E "(mAlwaysOnVpnPackage|mAlwaysOnVpnLockdown)"
# Expected: com.celzero.bravedns and true
```

---

## Step 11: Final Verification

### Check Device Owner
```bash
adb shell dumpsys device_policy | grep -A10 "Device Owner"
```
Should show `com.rosan.dhizuku`

### Check Common Criteria Mode
```bash
adb shell dumpsys device_policy | grep mCommonCriteriaMode
```
Should show `true`

### Check VPN Lockdown
```bash
adb shell dumpsys device_policy | grep -E "(mAlwaysOnVpnPackage|mAlwaysOnVpnLockdown)"
```
Should show `com.celzero.bravedns` and `true`

### Check Cellular State
```bash
adb shell dumpsys telephony.registry | grep "RegState"
```
Should show `POWER_OFF` (radio disabled for protection)

### Check Shizuku Status
Open Shizuku app → "Shizuku is running"

### Check LSPatch
Open LSPatch → Should show self-patched modules as active

### Check Modules Active
Open LSPatch → Modules tab → All modules should show "Activated"

### Check Debloat
```bash
adb shell pm list packages | grep -E "(google|oplus|qualcomm)"
```
Should show minimal packages

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

### Test F-Droid
1. Install F-Droid from [f-droid.org](https://f-droid.org)
2. Download and install any app
3. Should install without warnings

---

## Maintaining Your Freedom

### Block OTA Updates
```bash
# Via ADB
adb shell pm disable com.oppo.ota
adb shell pm disable com.google.android.update

# Via Canta
# Suspend OTA packages (do not remove completely)
```

### Freeze Play Services at Factory Version
```bash
# Prevent Play Services from updating
adb shell pm disable com.google.android.gms/.chimera.GmsIntentOperationService

# Or use VPN to block update servers:
# Add to firewall: *.google.com/update
```

### Keep Modules Updated
- Core Patch (new Android versions)
- LSPatch (framework updates)
- Xposed modules (bug fixes)
- DAX (when Dhizuku updates)

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
- Or use ADB mode to restart: `adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/files/start.sh`

### "System service not running" in LSPatch
- **This is normal** for no-root setups
- Modules still work system-wide via Shizuku
- Ignore this warning

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
- Embed DAX into Bootloader Spoofer for Device Owner authority
- Some banks use hardware attestation (cannot bypass)

### "Google Play Services required" error
- FakeGapps should handle this
- Verify FakeGapps is properly self-patched and enabled
- Check that Play Services is still present (factory version)
- Embed DAX into FakeGapps for higher authority

### Play Services keeps updating
```bash
# Disable auto-update
adb shell pm disable com.google.android.gms/.chimera.GmsIntentOperationService

# Block update servers via VPN/RethinkDNS
# Add these domains to blocklist:
# - android.clients.google.com
# - *.google.com/update
```

### Cellular radio won't turn on
- Sentry Radio may have it in POWER_OFF state
- Open Sentry Radio → Disable "Automatic Threat Mitigation" temporarily
- Or whitelist safe towers

---

## Proof: Dumpsys Output

Here is the actual `dumpsys device_policy` output from a successfully configured device:

```bash
$ adb shell dumpsys device_policy

Current Device Policy Manager state:
  Device Owner:
    admin=ComponentInfo{com.rosan.dhizuku/com.rosan.dhizuku.server.DhizukuDAReceiver}
    package=com.rosan.dhizuku
    isOrganizationOwnedDevice=true
    User ID: 0

  Enabled Device Admins (User 0):
    com.rosan.dhizuku/.server.DhizukuDAReceiver:
      policies:
        wipe-data
        reset-password
        limit-password
        force-lock
        set-global-proxy
        encrypted-storage
        disable-camera
      mCommonCriteriaMode=true

  Global Policies:
    UserRestrictionPolicyKey userRestriction_no_control_apps:
      BooleanPolicyValue { mValue= true }
    UserRestrictionPolicyKey userRestriction_no_config_cell_broadcasts:
      BooleanPolicyValue { mValue= true }
    UserRestrictionPolicyKey userRestriction_no_factory_reset:
      BooleanPolicyValue { mValue= true }
    UserRestrictionPolicyKey userRestriction_no_ultra_wideband_radio:
      BooleanPolicyValue { mValue= true }

Encryption Status: per-user
```

### What This Proves

| Setting | What It Confirms |
|---------|------------------|
| `Device Owner: com.rosan.dhizuku` | Dhizuku has highest privileges |
| `isOrganizationOwnedDevice=true` | Device appears as enterprise device |
| `mCommonCriteriaMode=true` | Government-grade security active |
| `no_control_apps=true` | Google cannot modify app settings |
| `no_config_cell_broadcasts=true` | Carrier updates blocked |
| `no_factory_reset=true` | Remote wipe prevented |
| `Encryption: per-user` | FBE active, boot requires password |

---

## Glossary

| Term | Meaning |
|------|---------|
| **ADB** | Android Debug Bridge - tool for communicating with Android devices |
| **AOSP** | Android Open Source Project - the open source core of Android |
| **Common Criteria Mode** | Government-grade security standard for enterprise devices |
| **DAX** | Dhizuku API for Xposed - grants Device Owner privileges to modules |
| **Device Owner** | Highest privilege level on Android (enterprise feature) |
| **FBE** | File-Based Encryption - encrypts files with user password |
| **FOSS** | Free and Open Source Software |
| **FRP** | Factory Reset Protection - Google's anti-theft system |
| **IMSI Catcher** | Fake cell tower used for surveillance (Stingray) |
| **LSPatch** | No-root Xposed framework for app modification |
| **MDM** | Mobile Device Management - enterprise device control |
| **OTA** | Over-The-Air - system updates delivered wirelessly |
| **Play Integrity API** | Google's device attestation system |
| **RIL** | Radio Interface Layer - communicates with cellular modem |
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
│  ✓ Common Criteria Mode active (government-grade security) │
│  ✓ Can install any APK (verified or not)                   │
│  ✓ Modified apps work (ReVanced, modded games)             │
│  ✓ Alternative stores work (F-Droid, Aurora)               │
│  ✓ Play Services at factory version + FakeGapps            │
│  ✓ Bootloader hidden (Netflix, banking work)               │
│  ✓ License verification bypassed (FuckGoogleLicense)       │
│  ✓ Modules have Device Owner authority (DAX embedded)      │
│  ✓ Encrypted with FBE (no boot-time verification)          │
│  ✓ Cellular attacks blocked (Sentry Radio)                 │
│  ✓ Network locked down (Owndroid + Rethink DNS)            │
│  ✓ Debloated (no spyware, no forced updates)               │
│  ✓ YOURS - not Google's                                    │
└─────────────────────────────────────────────────────────────┘
```

### Why Google Cannot "Fix" This
- **Device Owner** is an Android Enterprise API used by thousands of companies
- **Common Criteria Mode** is required for government and military devices
- **ADB** is a developer tool that cannot be removed
- **Xposed via LSPatch** uses legitimate app modification techniques
- **Your device appears as a compliant enterprise device**, not a hacked consumer phone
- Google cannot break these features without breaking Android for all enterprise customers

### When September 2026 Comes
```
Everyone else: "My phone won't install anything!"
You: "Everything works normally"

Everyone else: "Google blocked my apps!"
You: "I still have F-Droid, ReVanced, everything"

Everyone else: "I need to pay Google to develop!"
You: "I can still share apps with friends"

Everyone else: "My phone is being tracked via cellular!"
You: "Sentry Radio blocked the IMSI catcher"

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

This setup uses **legitimate Android enterprise APIs** and is intended for educational purposes. Device Owner is an official Android feature. Common Criteria Mode is an official security standard. No exploits, hacks, or reverse engineering are used.
