#!/usr/bin/env python3
"""
Android Freedom Setup - One Click Solution
WARNING: This performs FACTORY RESET! Backup your data first!
"""

import subprocess
import time
import os
import sys
import threading
from pathlib import Path

# Configuration
DHIZUKU_APK = "com.rosan.dhizuku.apk"  # Place this in same folder
TIMEOUT = 999999  # Wait forever
ADB_WAIT = 5  # Seconds between ADB checks

class Colors:
    """Terminal colors for better visibility"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    """Display the setup banner"""
    print(f"{Colors.BOLD}{Colors.BLUE}")
    print("=" * 60)
    print("   ANDROID FREEDOM SETUP - DEVICE OWNER ACTIVATOR")
    print("=" * 60)
    print(f"{Colors.END}")
    print(f"{Colors.YELLOW}⚠️  WARNING: This will FACTORY RESET your device!{Colors.END}")
    print(f"{Colors.YELLOW}⚠️  Backup ALL data before proceeding!{Colors.END}")
    print()

def run_command(cmd, timeout=None):
    """Run shell command and return output"""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True,
            timeout=timeout
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "", "Command timed out", -1
    except Exception as e:
        return "", str(e), -1

def wait_for_device(device_type="device", infinite=True):
    """
    Wait for ADB device with visual feedback
    device_type: "device" (booted) or "recovery" (recovery mode)
    infinite: True = wait forever, False = timeout after 300 seconds
    """
    print(f"{Colors.BOLD}Waiting for device in {device_type} mode...{Colors.END}")
    
    dots = 0
    start_time = time.time()
    timeout_seconds = 999999 if infinite else 300
    
    while True:
        # Check time
        if not infinite and (time.time() - start_time) > timeout_seconds:
            print(f"\n{Colors.RED}Timeout! Device not detected.{Colors.END}")
            return False
        
        # Get devices
        output, _, _ = run_command("adb devices")
        
        # Parse devices
        lines = output.strip().split('\n')[1:]  # Skip "List of devices attached"
        
        for line in lines:
            if '\t' in line:
                device_id, status = line.split('\t')
                if status == device_type:
                    print(f"\n{Colors.GREEN}✓ Device detected! ID: {device_id}{Colors.END}")
                    return True
        
        # Visual feedback
        dots = (dots + 1) % 4
        sys.stdout.write(f"\r{' ' * 60}\r")
        sys.stdout.write(f"Waiting for device{'.' * dots} ")
        sys.stdout.flush()
        time.sleep(1)

def factory_reset():
    """
    Perform factory reset via ADB
    This is the nuclear option - wipes everything
    """
    print(f"\n{Colors.BOLD}{Colors.RED}")
    print("=" * 60)
    print("   FACTORY RESET PHASE")
    print("=" * 60)
    print(f"{Colors.END}")
    print(f"{Colors.YELLOW}This will erase ALL data on your device!{Colors.END}")
    
    # Confirm with user
    confirm = input(f"{Colors.RED}Type 'YES' to continue: {Colors.END}")
    if confirm != "YES":
        print(f"{Colors.YELLOW}Cancelled.{Colors.END}")
        return False
    
    print(f"\n{Colors.BLUE}Attempting factory reset...{Colors.END}")
    
    # Method 1: Using am broadcast (works on most devices)
    print("Method 1: Using am broadcast...")
    cmd = 'adb shell "am broadcast -a android.intent.action.MASTER_CLEAR"'
    stdout, stderr, code = run_command(cmd)
    
    if code == 0 and "result=0" in stdout:
        print(f"{Colors.GREEN}✓ Factory reset initiated via broadcast{Colors.END}")
        return True
    
    # Method 2: Using settings (alternative)
    print("Method 2: Using settings command...")
    cmd = 'adb shell "settings put global factory_reset 1"'
    stdout, stderr, code = run_command(cmd)
    
    if code == 0:
        print(f"{Colors.GREEN}✓ Factory reset flag set. Reboot to reset...{Colors.END}")
        run_command("adb reboot")
        return True
    
    # Method 3: Using recovery mode command
    print("Method 3: Using recovery command...")
    cmd = 'adb shell "recovery --wipe_data"'
    stdout, stderr, code = run_command(cmd)
    
    if code == 0:
        print(f"{Colors.GREEN}✓ Recovery wipe command sent{Colors.END}")
        return True
    
    print(f"{Colors.RED}✗ All factory reset methods failed.{Colors.END}")
    print("Please manually factory reset your device through settings.")
    return False

def install_apk(apk_path):
    """Install APK via ADB"""
    print(f"\n{Colors.BLUE}Installing {apk_path}...{Colors.END}")
    
    if not os.path.exists(apk_path):
        print(f"{Colors.RED}✗ APK not found: {apk_path}{Colors.END}")
        return False
    
    stdout, stderr, code = run_command(f"adb install -r {apk_path}")
    
    if "Success" in stdout:
        print(f"{Colors.GREEN}✓ APK installed successfully{Colors.END}")
        return True
    else:
        print(f"{Colors.RED}✗ Installation failed: {stderr}{Colors.END}")
        return False

def set_device_owner(package_name, receiver_name):
    """
    Set Device Owner using dpm command
    Full path: com.rosan.dhizuku/.server.DhizukuDAReceiver
    """
    print(f"\n{Colors.BLUE}Setting Device Owner...{Colors.END}")
    
    full_component = f"{package_name}/{receiver_name}"
    cmd = f'adb shell dpm set-device-owner "{full_component}"'
    
    stdout, stderr, code = run_command(cmd)
    
    if "Already set" in stdout or "Device owner already set" in stdout:
        print(f"{Colors.GREEN}✓ Device Owner already set{Colors.END}")
        return True
    elif "Success" in stdout or "Device owner set successfully" in stdout:
        print(f"{Colors.GREEN}✓ Device Owner set successfully!{Colors.END}")
        return True
    else:
        print(f"{Colors.RED}✗ Failed to set Device Owner:{Colors.END}")
        print(f"  {stderr or stdout}")
        return False

def verify_setup():
    """Verify Device Owner is active"""
    print(f"\n{Colors.BLUE}Verifying Device Owner setup...{Colors.END}")
    
    stdout, _, code = run_command('adb shell dumpsys device_policy | grep -A5 "Device Owner"')
    
    if "com.rosan.dhizuku" in stdout:
        print(f"{Colors.GREEN}✓ Device Owner verified: Dhizuku is active!{Colors.END}")
        print(f"\n{Colors.BOLD}{Colors.GREEN}SETUP COMPLETE! Your device now has Device Owner privileges.{Colors.END}")
        return True
    else:
        print(f"{Colors.RED}✗ Device Owner verification failed{Colors.END}")
        return False

def adb_input(text):
    """Send keyboard input via ADB"""
    run_command(f'adb shell input text "{text}"')

def adb_tap(x, y):
    """Tap screen coordinates via ADB"""
    run_command(f"adb shell input tap {x} {y}")

def interactive_setup():
    """Interactive setup for devices that need manual confirmation"""
    print(f"\n{Colors.YELLOW}Some devices require manual confirmation for factory reset.{Colors.END}")
    print("If a confirmation screen appears on your device:")
    print("  1. Look at your phone screen")
    print("  2. Tap 'OK' or 'Confirm' when prompted")
    print()
    
    confirm = input("Ready? (Press Enter to continue, or 'skip' to skip this step): ")
    if confirm.lower() == 'skip':
        return
    
    # Attempt to tap the confirmation button (common coordinates)
    # Many devices have confirmation at center or bottom
    print("Attempting to tap confirmation button...")
    adb_tap(540, 1800)  # Common bottom center
    time.sleep(1)
    adb_tap(540, 1200)  # Common center
    time.sleep(1)
    adb_tap(540, 900)   # Common lower center

def main():
    """Main execution flow"""
    print_banner()
    
    # Check if ADB is installed
    print(f"{Colors.BLUE}Checking ADB...{Colors.END}")
    _, _, code = run_command("adb version")
    if code != 0:
        print(f"{Colors.RED}✗ ADB not found. Please install Android SDK Platform Tools.{Colors.END}")
        print("  Download from: https://developer.android.com/studio/releases/platform-tools")
        sys.exit(1)
    print(f"{Colors.GREEN}✓ ADB found{Colors.END}")
    
    # Check if Dhizuku APK exists
    if not os.path.exists(DHIZUKU_APK):
        print(f"{Colors.YELLOW}⚠️  Dhizuku APK not found: {DHIZUKU_APK}{Colors.END}")
        print(f"   Please download Dhizuku APK and place it in this folder.")
        print(f"   Download from: https://github.com/iamr0s/Dhizuku/releases")
        choice = input(f"Continue anyway? (y/n): ")
        if choice.lower() != 'y':
            sys.exit(1)
    
    # Step 1: Wait for initial device connection
    print(f"\n{Colors.BOLD}STEP 1: Connect your device{Colors.END}")
    print("Enable USB Debugging on your phone:")
    print("  Settings → About Phone → Tap Build Number 7 times")
    print("  Settings → Developer Options → Enable USB Debugging")
    print()
    
    if not wait_for_device("device", infinite=True):
        print(f"{Colors.RED}Cancelled.{Colors.END}")
        sys.exit(1)
    
    # Step 2: Factory Reset
    print(f"\n{Colors.BOLD}STEP 2: Factory Reset{Colors.END}")
    print(f"{Colors.RED}⚠️  THIS WILL WIPE ALL DATA! ⚠️{Colors.END}")
    
    if not factory_reset():
        print(f"{Colors.YELLOW}Manual factory reset required.{Colors.END}")
        print("Please manually reset your device, then press Enter when done.")
        input()
    
    # Step 3: Wait for device to reset and reboot
    print(f"\n{Colors.BOLD}STEP 3: Waiting for device after reset{Colors.END}")
    print("Device will reboot. This may take 5-10 minutes...")
    
    # Wait for device to disappear (reset in progress)
    print("Waiting for device to disconnect...")
    while True:
        stdout, _, _ = run_command("adb devices")
        if "device" not in stdout or "unauthorized" in stdout:
            break
        time.sleep(ADB_WAIT)
    
    print("Device disconnected. Waiting for it to come back...")
    
    # Wait for device to reappear in recovery mode
    if not wait_for_device("recovery", infinite=True):
        print("Recovery mode not detected. Waiting for booted device...")
        wait_for_device("device", infinite=True)
    
    # Step 4: Wait for full boot
    print(f"\n{Colors.BOLD}STEP 4: Waiting for device to fully boot{Colors.END}")
    print("This may take several minutes. Do not interrupt...")
    
    # Wait for boot completion
    while True:
        stdout, _, _ = run_command("adb shell getprop sys.boot_completed")
        if "1" in stdout:
            break
        time.sleep(5)
        print("  Still booting...")
    
    print(f"{Colors.GREEN}✓ Device fully booted{Colors.END}")
    time.sleep(5)  # Extra wait for system to stabilize
    
    # Step 5: Install Dhizuku APK
    print(f"\n{Colors.BOLD}STEP 5: Install Dhizuku{Colors.END}")
    
    if not install_apk(DHIZUKU_APK):
        print(f"{Colors.RED}Failed to install Dhizuku.{Colors.END}")
        sys.exit(1)
    
    # Step 6: Set Device Owner
    print(f"\n{Colors.BOLD}STEP 6: Set Device Owner{Colors.END}")
    
    if not set_device_owner("com.rosan.dhizuku", ".server.DhizukuDAReceiver"):
        print(f"{Colors.YELLOW}Attempting alternative method...{Colors.END}")
        # Some devices need the full path differently
        if not set_device_owner("com.rosan.dhizuku", "com.rosan.dhizuku.server.DhizukuDAReceiver"):
            print(f"{Colors.RED}Device Owner setup failed.{Colors.END}")
            sys.exit(1)
    
    # Step 7: Verify
    print(f"\n{Colors.BOLD}STEP 7: Verification{Colors.END}")
    
    if verify_setup():
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'=' * 60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.GREEN}   SUCCESS! Device Owner is now ACTIVE!{Colors.END}")
        print(f"{Colors.BOLD}{Colors.GREEN}{'=' * 60}{Colors.END}")
        print(f"\n{Colors.BOLD}Next steps:{Colors.END}")
        print("  1. Install Shizuku from F-Droid or Google Play")
        print("  2. Enable Wireless Debugging in Developer Options")
        print("  3. Pair Shizuku with your device")
        print("  4. Install LSPatch and modules")
        print("  5. Debloat with Canta")
        print("  6. Set FBE with locksettings command")
        print()
        print(f"{Colors.BOLD}Your device now has permanent Device Owner privileges!{Colors.END}")
        print("Google cannot override these privileges.")
    else:
        print(f"\n{Colors.RED}Setup incomplete. Please check manually.{Colors.END}")
        print("Run: adb shell dumpsys device_policy")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Interrupted by user{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")
        sys.exit(1)
