import Mondule
import sys

print(""" 
                -----Software List :
                |     [0] :   Chrome
                |     [1] :   Libre Office
                |     [2] :   Virtual Box
                |     [3] :   Visual Studio Code
                |     [4] :   Calibre
  Auto Mode ==  |     [5] :   Gimp
                |     [6] :   OBs Studio     
                |     [7] :   MongoDB
                |____ [8] :   Atom

                      
                      [9] :   Xmapp
                      [10]:   Openshot
                      [11]:   Shotcut
                      [12]:   Sublime Text
                      [13]:   audacity
    Developed By h4n24wnyin3


    [01] : Auto       [02] : Manual     [00] : Exit   [HanZaw] : About [mm] : Myanmar Font 

""")

UserChoose = input("Enter Your Choose  :")


if UserChoose == '0' :
   Mondule.Chrome()
elif UserChoose == '1':
    Mondule.LibreOffice()
elif UserChoose == '2':
     Mondule.VirtualBox()
elif UserChoose == '3':
    Mondule.VisualStudioCode()
elif UserChoose == '4':
    Mondule.Calibre()
elif UserChoose == '5':
    Mondule.Gimp()
elif UserChoose == '6':
    Mondule.OBS()
elif UserChoose == '7':
    Mondule.MongoDB()
elif UserChoose == '8':
    Mondule.Atom()
elif UserChoose == '9':
    Mondule.xmapp()
elif UserChoose == '10':
    Mondule.Openshot()
elif UserChoose == '11':
    Mondule.shotcut()
elif UserChoose == '12':
    Mondule.SublimeText()
elif UserChoose == '13':
    Mondule.audacity()
elif UserChoose == '01':
    print("""
                [01] : Auto 

            -----Software List :
                |     [0] :   Chrome
                |     [1] :   Libre Office
                |     [2] :   Virtual Box
                |     [3] :   Visual Studio Code
                |     [4] :   Calibre
  Auto Mode ==  |     [5] :   Gimp
                |     [6] :   OBs Studio     
                |     [7] :   MongoDB
                |____ [8] :   Atom
    """)
    Mondule.Chrome()
    Mondule.LibreOffice()
    Mondule.VirtualBox()
    Mondule.VisualStudioCode()
    Mondule.Calibre()
    Mondule.Gimp()
    Mondule.OBS()
    Mondule.MongoDB()
    Mondule.Atom()

elif UserChoose == '02':
    print(""" 
     [02] : Manual
     """)
    a = input("Enter Your Choose (Example - 1,2,3,4,etc... :")    
    Mondule.Manual(a)
elif UserChoose == '00':
    print("Exit")
    sys.exit()
elif UserChoose == 'HanZaw':
    print("About")
    print("Github - https://github.com/HanZawNyine")
    print("Facebook - https://www.facebook.com/H4n24wNyin3/ ")
elif UserChoose == 'mm':
    Mondule.MyanmarFont()

else:
    print("Error Input")
    
print("Developed By h4n24wnyin3")

    
