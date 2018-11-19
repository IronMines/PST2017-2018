Raspberry Pi Configuration (software)
==
**First of all, the WIFI needs to be `disabled` at the competition time**

---

# OS installation (on your personal computer)
**Requires  `root` rights**

**/!\ Take care with `dd` command, it might wipe-off all your personal datas in case of wrong parameters./!\**
**Use `fdisk -l`, `df -h` and/or `dmesg` in order to locate correct devices to use.**

1. Download the RPi OS `raspbian` at this page : https://www.raspberrypi.org/downloads/raspbian/

2. Decompile the ISO on a microSD support :

	```bash
dd bs=4M if=/path/to/the/iso of=/dev/micro_sd_dev conv=fsync
	```

# Configuration
**Requires  `root` rights**

Execute `raspi-config` on the rapsberry, then :

 1. Configure the layout to fit your country
 2. Enable SSH
 3. **Disable Serial Console and enable Serial hardware**

# Install dependencies
**Requires  `root` rights**

Execute :

```bash
apt update
apt upgrade
apt install python python-pip mc ranger fail2ban dnsmask hostapd screen wiringpi
# And for Pharo
apt install libgl1-mesa-glx libsm6 libice6
```

Detail of theses packages:
* `mc` / `ranger` : A console interface to navigate in folders
* `python` : An interpreter for python
* `hostapd` : A daemon to create a WIFI hotspot on the RPi
* `dnsmask` : A DHCP and DNS server to avoid manual configuration of network on RPi hotspot's  clients
* `fail2ban` : A ISP to block attacks on SSH
* `screen` : To read/write on Serial port and to be able to manage multiple shell
* `wiringpi` : GPIO Interface library for the Raspberry Pi

Required for `Pharo` :
* `libgl1-mesa-glx` : A free implementation of the OpenGL API
* `libsm6` : X11 Session Management library
* `libice6` : X11 Inter-Client Exchange library


# Configure Power Down button
**Requires  `root` rights**

 1. Add the script `/root/power_off_button.py` on the system

 2. Add execution rights on this file :

	```bash
chmod a+x /root/power_off_button.py
	```
 3. Launch this script when the RPi boot up :

	```bash
nano /system_disk/etc/rc.local
	```

# Install Pharo

 1. Download `pharo` at this url : http://files.pharo.org/vm/pharo-spur32/linux/armv6/latest.zip

	```bash
mkdir ~/pharo/
cd ~/pharo/
wget http://files.pharo.org/vm/pharo-spur32/linux/armv6/latest.zip
unzip latest.zip
	```
 2. Download images for `pharo` at this url : http://files.pharo.org/image/50/latest.zip

	```bash
 mkdir ~/pharo-vm/
 cd ~/pharo-vm/
 wget http://files.pharo.org/image/50/latest.zip
 unzip latest.zip
	```

 3. Install libraries on this image

	```bash
# Use -X option of ssh to remote X-display : ssh -X pi@192.168.0.1
~/pharo/pharo ~/pharo-vm/[image_name_here].image
	```

	In the `playground` :

	```smalltalk
Metacello new
	baseline: 'PharoThings';
	repository: 'github://pharo-iot/PharoThings/src';
	load: #(RemoteDevServer Raspberry).
ClySystemEnvironmentPlugin disableSlowPlugins.
	```

	Then save your image as `rpi.image`.

 4. Run `pharo` with this command (except `--headless` meaning without graphical interface, `args` are explicit ):

	```bash
~/pharo/pharo --headless ~/pharo-vm/rpi.image remotePharo --startServerOnPort=8888
	```
