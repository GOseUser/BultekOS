# Import needed modules
import os
import shutil
import requests
response = requests.get('https://google.com/')
def main():
    # Ask for Desktop Environment
    de = -1
    while de<=0 or de>=5:
        de = int(input("Desktop Environment: 1) GNOME 2) KDE 3) Cutefish 4) Budgie \n "))
        if de==1:
            desktop="gnome gnome-extra"
        if de==2:
            desktop="plasma-meta kde-applications-meta gdm kvantum-qt5"
        if de==3:
            desktop="cutefish gdm"
        else:
            desktop="gnome gnome-extra budgie-desktop"
    # Ask for AUR helper
    aurhelper = 2
    while aurhelper<=0 or aurhelper>=4:
        aurhelper = input("1) yay 2) paru 3) none \n ")
        if aurhelper==1:
            aur = "yay"
        if aurhelper==2:
            aur = "paru"
        else:
            aur = "";
    # Partitions
    print("Do you want to open GPARTED? y/n")
    dopartition="n"
    dopartition=input()
    if dopartition=="n" or dopartition=="no":
        pass
    else:
        os.system("gparted")
    os.system("lsblk")
    rootpart=input("Enter root partition: ")
    while os.file.exists(rootpart)==False:
        rootpart=input("Enter root partition: ")
    else:
        bootpart=input("Enter boot partition: ")
        while os.file.exists(bootpart)==False:
            bootpart=input("Enter boot partition: ")
        # Setup new user info
        else:
            print("You are going to configure a new user")
            username=input("Please enter username (IT MUST BE ONLY NON CAPITAL LETTERS): ")
            #password=input("Please enter a password: ")
        # Be ready for installation
        os.system("mkfs.btrfs -q -f "+rootpart)
        os.system("mkfs.vfat "+bootpart)
        os.system("mkdir -p /mnt/bultekroot")
        os.system("mount "+rootpart+" /mnt/bultekroot")
        os.system("mkdir -p /mnt/bultekroot/boot")
        os.system("mount "+bootpart+" /mnt/bultekroot/boot")
        os.system('pacstrap /mnt/bultekroot base linux-zen linux-zen-headers linux-firmware networkmanager discord opendoas firefox git nano python3 libreoffice-fresh neofetch alacritty networkmanager flatpak steam lutris code gimp discord telegram-desktop ntfs-3-dkms '+desktop+' '+aur+' --noconfirm')
        os.system('chroot /mnt/bultekroot "systemctl enable gdm.service -f && systemctl enable NetworkManager.service && grub-install --bootloader-id=BultekOS"')
        os.system('useradd -R /mnt/bultekroot -G wheel -s /bin/zsh -m -l '+username)
        print("Please enter password for account: " + username)
        os.system('passwd -R /mnt/bultekroot '+username)
if response.status_code == 200:
    main();
else:
    print("FATAL ERROR: NO INTERNET CONNECTION!")