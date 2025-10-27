# network_scanner.py
"""
Simple Network Scanner
I built this to practice my Python skills while combining my electrical background with cybersecurity.

It's basically a digital version of tracing wires in a building - but for finding devices on a network!
"""

import socket
import subprocess
import platform
from datetime import datetime

def scan_my_network():
    """Scan the local network to see what's connected"""
    print("Starting network scan...")
    print("This is like checking what devices are plugged in, but for your WiFi!")
    
    # Figure out what network we're on
    hostname = socket.gethostname()
    my_ip = socket.gethostbyname(hostname)
    network_base = '.'.join(my_ip.split('.')[:-1])  # Get first 3 parts of IP
    
    print(f"Looking for devices on: {network_base}.1-254")
    
    # Check each possible IP address
    found_devices = []
    for last_octet in range(1, 20):  # Just check first 20 to keep it quick
        target_ip = f"{network_base}.{last_octet}"
        
        try:
            # Ping the device (like tapping on a wire to see if it's live)
            if platform.system().lower() == "windows":
                command = ["ping", "-n", "1", "-w", "1000", target_ip]
            else:
                command = ["ping", "-c", "1", "-W", "1", target_ip]
                
            # Run the ping and check response
            response = subprocess.call(command, 
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL)
            
            if response == 0:  # If device responded
                found_devices.append(target_ip)
                print(f"Found device at: {target_ip}")
                
        except Exception as e:
            print(f"Had trouble checking {target_ip}: {e}")
    
    return found_devices

def give_security_tips(devices):
    """Give practical security advice based on what we found"""
    print("\n" + "="*50)
    print("SECURITY TIPS FROM AN ELECTRICIAN'S PERSPECTIVE:")
    print("="*50)
    
    if not devices:
        print("No devices found - might want to check your network connection!")
        return
    
    print(f"Found {len(devices)} devices on your network")
    
    for device in devices:
        print(f"\nFor device at {device}:")
        print("• Change any default passwords (like changing lock cylinders)")
        print("• Keep software updated (like maintaining electrical panels)")
        print("• Consider putting IoT devices on a separate network")
        print("• Physically check unknown devices (trust but verify!)")

def main():
    print("🔌 Network Device Scanner")
    print("Built by an electrician learning cybersecurity")
    print("This tool helps you see what's connected to your network\n")
    
    input("Press Enter to start scanning...")
    
    devices = scan_my_network()
    give_security_tips(devices)
    
    print(f"\nScan complete! Found {len(devices)} active devices.")
    print("\nJust like tracing electrical circuits, knowing what's on your")
    print("network is the first step to securing it!")

if __name__ == "__main__":
    main()
