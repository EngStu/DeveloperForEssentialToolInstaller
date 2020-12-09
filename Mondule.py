import os
import sys
import requests

def Chrome():
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo apt install ./google-chrome-stable_current_amd64.deb -y")
    os.system("# google-chrome --no-sandbox")
    os.system("sudo rm -r google-chrome-stable_current_amd64.deb")

def LibreOffice():
    os.system("sudo apt install libreoffice -y")

def VirtualBox():
    os.system("sudo wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -")
    os.system("sudo wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -")
    os.system("""sudo  echo "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian buster contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list """)
    os.system("sudo apt-get install virtualbox -y")

def VisualStudioCode():
    os.system("wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg")
    os.system("sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/")
    os.system("""sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'""")
    os.system("sudo apt-get install apt-transport-https")
    os.system("sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove -y" )
    os.system("sudo apt-get install code -y") 
    os.system ("rm -r packages.microsoft.gpg")

def Calibre():
    os.system("sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin")

def Gimp():
    os.system("sudo apt-get install gimp -y")

def OBS():
    os.system("sudo apt install ffmpeg -y")
    os.system("sudo apt install obs-studio -y")

def MongoDB():

    #os.system("wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -")
    os.system("sudo apt-get install gnupg")
    os.system("wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -")
    os.system("""echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list""")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y mongodb-org")
    os.system("""
    echo "mongodb-org hold" | sudo dpkg --set-selections
    cho "mongodb-org-server hold" | sudo dpkg --set-selections
    echo "mongodb-org-shell hold" | sudo dpkg --set-selections
    echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
    echo "mongodb-org-tools hold" | sudo dpkg --set-selections
    """)
    os.system("ps --no-headers -o comm 1")
    os.system("sudo systemctl start mongod")
    os.system("sudo systemctl daemon-reload")
    #os.system("sudo systemctl status mongod")
    os.system("sudo systemctl enable mongod")
    os.system("sudo systemctl stop mongod")
    os.system("sudo systemctl restart mongod")
    #os.system("mongo")
    os.system("exit")

    os.system("wget https://downloads.mongodb.com/compass/mongodb-compass_1.23.0_amd64.deb")
    os.system("sudo dpkg -i mongodb-compass_1.23.0_amd64.deb")
    os.system("mongodb-compass")
    os.system("sudo rm -r mongodb-compass_1.23.0_amd64.deb ")

def Atom():
    os.system("wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -")
    os.system(""" sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list' """)
    os.system("sudo apt-get update")
    os.system("sudo apt-get install atom -y " )
    #os.system("sudo apt-get install atom-beta")

def DownloadXmapp(url,Downloadd):
        r = requests.get(url, allow_redirects=True)
        open(Downloadd, 'wb').write(r.content)
        os.system("chmod 755 "+Downloadd)  


def xmapp():
    print("""
                        XAMPP for Linux 7.2.34, 7.3.25, 7.4.13 & 8.0.0
                ===================================================================
                Version	    	        Checksum		                      Size
                ---------------------------------------------------------------------
            [1] 7.2.34 / PHP 7.2.34	    md5 sha1        Download (64 bit)     151 Mb
            [2] 7.3.25 / PHP 7.3.25     md5 sha1        Download (64 bit)	  150 Mb
            [3] 7.4.13 / PHP 7.4.13		md5 sha1        Download (64 bit) 152 Mb
            [4] 8.0.0 / PHP 8.0.0	    md5 sha1        Download (64 bit)     150 Mb
            [0] Exit

    """)

    Version = input("Enter Your Choose :")
    
    
    if Version == '1':
        print("Wait a moment Please ......................................")  
        print("[1] 7.2.34 / PHP 7.2.34	    md5 sha1        Download (64 bit)     151 Mb")
        DownloadXmapp("https://www.apachefriends.org/xampp-files/7.2.34/xampp-linux-x64-7.2.34-0-installer.run","xampp-linux-x64-7.2.34-0-installer.run") 
        os.system("sudo ./xampp-linux-x64-7.2.34-0-installer.run")
        os.system("sudo rm -r xampp-linux-x64-7.2.34-0-installer.run") 
        

    elif Version == '2':
        print("Wait a moment Please ......................................")
        print("[2] 7.3.25 / PHP 7.3.25     md5 sha1        Download (64 bit)	  150 Mb")
        DownloadXmapp("https://www.apachefriends.org/xampp-files/7.3.25/xampp-linux-x64-7.3.25-0-installer.run","xampp-linux-x64-7.3.25-0-installer.run") 
        os.system("sudo ./xampp-linux-x64-7.3.25-0-installer.run")
        os.system("sudo rm -r 7.3.25/xampp-linux-x64-7.3.25-0-installer.run")  
        

    elif Version == '3':
        print("Wait a moment Please ......................................")
        print("[3]  7.4.13 / PHP 7.4.13		md5 sha1        Download (64 bit)	  152 Mb")
        DownloadXmapp("https://www.apachefriends.org/xampp-files/7.4.13/xampp-linux-x64-7.4.13-0-installer.run","xampp-linux-x64-7.4.13-0-installer.run") 
        os.system("sudo ./xampp-linux-x64-7.4.13-0-installer.run")
        os.system("sudo rm -r xampp-linux-x64-7.4.13-0-installer.run")  
        
    elif Version == '4':
        print("Wait a moment Please ......................................")
        print("[4] 8.0.0 / PHP 8.0.0	    md5 sha1        Download (64 bit)     150 Mb")
        DownloadXmapp("https://www.apachefriends.org/xampp-files/8.0.0/xampp-linux-x64-8.0.0-0-installer.run","xampp-linux-x64-8.0.0-0-installer.run") 
        os.system("sudo ./xampp-linux-x64-8.0.0-0-installer.run")
        os.system("sudo rm -r xampp-linux-x64-8.0.0-0-installer.run")   
        
    elif Version == '0':
        sys.exit()
         
    else :
        xmapp()

def Openshot():
    os.system("sudo apt-get install openshot -y ")

def shotcut():
    os.system("sudo apt install shotcut -y")


def SublimeText():
    os.system("wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -")
    os.system("sudo apt-get install apt-transport-https")
    os.system(""" echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list""")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install sublime-text -y")

def audacity():
    os.system("sudo apt-get install audacity -y")

def Manual(a):
    UserChoose = 0
    
    for UserChoose in Convert(a):
        print(UserChoose)
        #print(UserChoose)
        if UserChoose == '0' :
            print("Chrome")
            Chrome()
        elif UserChoose == '1':
            print("LibreOffice")
            LibreOffice()
        elif UserChoose == '2':
            print("Virtual Box")
            VirtualBox()
        elif UserChoose == '3':
            print("Visual Studio Code")
            VisualStudioCode()
        elif UserChoose == '4':
            print("Calbire")
            Calibre()
        elif UserChoose == '5':
            print("Gimp")
            Gimp()
        elif UserChoose == '6':
            print("OBS Studio")
            OBS()
        elif UserChoose == '7':
            print(MongoDB)
            MongoDB()
        elif UserChoose == '8':
            print("Atom")
            Atom()
        elif UserChoose == '9':
            print("XMAPP")
            xmapp()
        elif UserChoose == '10':
            print("Open Shot")
            Openshot()
        elif UserChoose == '11':
            print("Shotcut")
            shotcut()
        elif UserChoose == '12':
            print("Sublime Text")
            SublimeText()
        elif UserChoose == '13':
            print("audacity")
            audacity()
        else:
            print("False Arguments & Exit..............")
    return UserChoose

def Convert(string): 
    li = list(string.split(",")) 
    return li

def MyanmarFont():
    os.system("sudo bash aa.sh")
    os.system("sudo rm -r mm-kb-master")



