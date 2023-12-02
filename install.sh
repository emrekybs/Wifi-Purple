sudo apt update
sudo apt-get install -y mdk3
sudo apt-get install -y xterm
sudo apt-get install -y aircrack-ng
sudo apt-get install -y bully
sudo apt-get install -y wifite
clear

if [ $? -eq 0 ]; then
    echo -e "\033[1;35mInstallation successful!\033[0m"
    
    sleep 2
    

    clear
    sudo python3 wifi-purple.py
else
    echo "Installation failed."
fi
