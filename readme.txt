Info
This is intended to run on a RaspberryPi Zero.
The Pi Zero should be in AP mode.
Connect to the Pi Zero's wireless network.
Then access the server at http://192.168.4.1:8000

How to setup the Pi Zero
1. Follow instructions online to set the Pi up for AP (access point) mode.
2. Modify "/etc/dhcpcd.conf" adding this to the bottom:
interface wlan0
  static ip_address=192.168.4.1/24
  nohook wpa_supplicant

How to setup the project locally
1. If on Windows, start a linux instance in the terminal. Run "wsl"
2. Navigate to the project folder.
3. Run "python -m venv venv" to create a virtual environment.
4. You should now have a venv folder
5. Activate the virtual environment by running "source venv/bin/activate"
6. Run pip install -r requirements.txt (this isntalls packages in the venv)
7. Exit the venv with "deactivate"
8. Start using "make server".

How to run the server (locally or on pi)
1. If on Windows, start a linux instance in the terminal. Run "wsl"
2. Navigate to the project folder.
3. For development run "make dev". For production run "make server".
