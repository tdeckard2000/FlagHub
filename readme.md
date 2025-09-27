### Info
This is intended to run on a RaspberryPi Zero.
It is the FlagHub software that acts as the central access point for all FlagCams.

End devices (FlagCams) connect to the Pi Zero's wireless network (AP).
Then access the server at http://192.168.4.1:8000

### How to setup the Pi Zero
First, we need to delay initialization of the external PAU09 USB WiFi module (used as an AP).
This prevents a conflict with the onboard WiFi adapter (used as a standard client).
1. Modify '/etc/rc.local' to add these lines above 'exit 0'.
  sleep 15
  modprobe rt2800usb
  sleep 5
  systemctl start hostapd
  systemctl start dnsmasq
2. Ensure hostapd and dnsmasq auto initialization is disabled by running this command.
  sudo systemctl disable hostapd && sudo systemctl disable dnsmasq
3. Create a file named 'blacklist.conf' at '/etc/modprobe.d/blacklist.conf' then add this line.
  blacklist rt2800usb

Next, we need to setup the wifi credentials.
1. 'sudo vi /etc/wpa_supplicant/wpa_supplicant.conf' (file appears blank without sudo)
  The whole file should look like this:
  country=US
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1

  network={
    ssid="your_wifi_ssid"
    psk="your_wifi_passkey"
  }
2. Update '/etc/dhcpcd.conf', adding this to the bottom.
  interface wlan 0

  interface wlan1
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
3. We need to setup things for the external wifi adapter.
  Modify 'etc/dnsmasq.conf' tp add:
  interface=wlan1
  dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
4. We need to add credentials for accessing the AP.
  Modify '/etc/hostapd/hostapd.conf' to add:
  interface=wlan1
  driver=nl80211
  ssid=FlagHub
  hw_mode=g
  channel=7
  wmm_enabled=0
  auth_algs=1
  wpa=2
  wpa_passphrase=123456 (enter whatever password you want for the AP)
  wpa_key_mgmt=WPA-PSK
  rsn_pairwise=CCMP

### How to setup the project locally
1. If on Windows, start a linux instance in the terminal. Run "wsl"
2. Navigate to the project folder.
3. Run "python -m venv venv" to create a virtual environment.
4. You should now have a venv folder
5. Activate the virtual environment by running "source venv/bin/activate"
6. Run pip install -r requirements.txt (this isntalls packages in the venv)
7. Exit the venv with "deactivate"
8. Start using "make server".

### How to run the server (locally or on pi)
1. If on Windows, start a linux instance in the terminal. Run "wsl"
2. Navigate to the project folder.
3. For development run "make dev". For production run "make server".

### Deploy changes to FlagHub (RaspberryPi)
1. Copy the python file to FlagHub 'scp server.py piClient/main'.
2. Restart the app on FlagHub.
  - SSH into the FlagHub 'ssh piClient' 
  - Run 'make killServer' to stop the server.
  - Reboot the FlagHub to start the server up again normally, or run 'make server' to watch logs.
  - 