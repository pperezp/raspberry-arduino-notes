# apuntes_raspberry2

https://www.raspberrypi.org
http://www.raspberryshop.es
http://sourceforge.net/projects/win32diskimager

http://www.frambuesapi.co/2013/10/07/conexion-remota-al-raspberry-pi-usando-vnc/


## IP estática
sudo nano /etc/network/interfaces
Remove the line that reads
iface eth0 inet dhcp
Add the following
iface eth0 inet static
address 192.168.1.10
netmask 255.255.255.0
network 192.168.1.0
broadcast 192.168.1.255
gateway 192.168.1.1


## SSH
http://cplus.about.com/od/raspberrypi/a/How-Do-I-Setup-Ssh-On-Raspberry-Pi.htm

## VNC Viewer
sudo apt-get install tightvncserver
vncserver :1 -geometry 1280x720 -depth 16 -pixelformat rgb565

## VNC VIEWER EN BOOT
cd /etc/init.d/
// pegar vncboot.sh
sudo chmod 755 vncboot.sh
sudo update-rc.d lightdm remove
sudo update-rc.d vncboot.sh defaults

## Dejar VNC SERVER al arranque
https://www.raspberrypi.org/documentation/remote-access/vnc/

## FTP
https://geekytheory.com/tutorial-raspberry-pi-9-servidor-ftp/
http://www.linuxhispano.net/2011/02/07/configurar-vsftp-para-conexiones-seguras-tlssslsftp/

## LAMP
https://wiki.debian.org/LaMp

# MySQL
sudo apt-get install mysql-server --fix-missing
CREATE USER 'pperezp'@'%' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'pperezp'@'%';
FLUSH PRIVILEGES;

sudo nano /etc/mysql/my.cnf
comentar la siguiente linea
bind-address          = 127.0.0.1

## Test conexión (Terminal)
mysql -u prez -h 192.168.0.20 -p

## Respaldar EL SO de la SD
http://raspberrypi.stackexchange.com/questions/311/how-do-i-backup-my-raspberry-pi
### Backup
dd if=/dev/sdx of=/path/to/image bs=1M
Where /dev/sdx is your SD card.

### Restore
dd if=/path/to/image of=/dev/sdx

## BORRAR SD CARD DESPUÉS DE INSTALAR SO
http://raspberrypi.stackexchange.com/questions/1446/how-can-i-reformat-my-sd-card-to-use-it-normally-again

cmd
diskpart
LIST DISK
SELECT DISK # (where # is the SD card)
CLEAN
CREATE PARTITION PRIMARY
FORMAT FS=NTFS QUICK
ASSIGN

# No DNS (duckdns)
https://www.duckdns.org/install.jsp?tab=pi 
