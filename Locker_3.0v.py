import subprocess
from datetime import datetime
import getpass
import base64

def option():
    print("""\033[1;34;40m
    


 LLLLLLLLLLL                                                  kkkkkkkk                                                
L:::::::::L                                                  k::::::k                                                
L:::::::::L                                                  k::::::k                                                
LL:::::::LL                                                  k::::::k                                                
  L:::::L                  ooooooooooo       cccccccccccccccc k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  L:::::L                oo:::::::::::oo   cc:::::::::::::::c k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r  
  L:::::L               o:::::::::::::::o c:::::::::::::::::c k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r 
  L:::::L               o:::::ooooo:::::oc:::::::cccccc:::::c k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::r
  L:::::L               o::::o     o::::oc::::::c     ccccccc k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::r
  L:::::L               o::::o     o::::oc:::::c              k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrr
  L:::::L               o::::o     o::::oc:::::c              k:::::::::::k  e::::::eeeeeeeeeee   r:::::r            
  L:::::L         LLLLLLo::::o     o::::oc::::::c     ccccccc k::::::k:::::k e:::::::e            r:::::r            
LL:::::::LLLLLLLLL:::::Lo:::::ooooo:::::oc:::::::cccccc:::::ck::::::k k:::::ke::::::::e           r:::::r            
L::::::::::::::::::::::Lo:::::::::::::::o c:::::::::::::::::ck::::::k  k:::::ke::::::::eeeeeeee   r:::::r            
L::::::::::::::::::::::L oo:::::::::::oo   cc:::::::::::::::ck::::::k   k:::::kee:::::::::::::e   r:::::r            
LLLLLLLLLLLLLLLLLLLLLLLL   ooooooooooo       cccccccccccccccckkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr
   
                                    localhost
   

                    [+] https://www.youtube.com/channel/UCCW_VavS78MbCu-JmLaAyXA
                    [+] Vanuja Janadith
                    [+] Coded_by_PASINDU_SANDEEPA
                    [@] bombtiktiktik54321@gmail.com


    [+] 1.Hide folder or file
    [+] 2.Unhide folder or file
    [+] 3.History
    [+] 4.Setting
    [+] 0.Exit
    """)

def main():
    path=0
    start_check()
    active="run"
    while active=="run":
        option()
        choice=input("\033[1;33;40m>> \033[1;31;40m").lower()
        if choice=="1":
            hide(path)
        elif choice=="2":
            unhide(path)
        elif choice=="3":
            historyR()
        elif choice=="4":
            #sec()
            if sec()==1:
                setting()
        elif choice=="0":
            active="exit"
        elif choice[0:8]=="set path":
            path=choice[9:]
            print("\033[1;34;40mpath = {0}".format(path))
        subprocess.call("cls",shell=True)

def start_check():
    file=open("pass.txt","r")
    file_line=file.readlines()
    if file_line[2]=="1\n":
        #sec()
        if sec()==1:
            print("\033[1;34;40m[+] Login sucsess..")
        else:
            print("\033[1;31;40m[!] Passwd incorrect..")
            quit()
    else:
        print("[+] Saved login")
        print(file_line[2])



def hide(path):
    if path==0:
        print("\033[1;31;40m[+] Please set path ex:- set path c:\ user\ admin\ log.txt")
    else:
        path=path.replace("\ ","\\")
        command='attrib +r +s +h "{0}" /S /D /L'.format(path)
        subprocess.call(command,shell=True)
        now=datetime.now()
        dt=now.strftime("%Y/%m/%d <--> %H:%M:%S")
        history="[+] Hide   | {0} | {1}\n".format(dt,path)
        hisfile=open("his.txt","a")
        hisfile.write(history)
        hisfile.close()

def unhide(path):
    if path==0:
        print("\033[1;31;40m[+] Please set path ex:- set path c:\ user\ admin\ log.txt")
    else:
        path=path.replace("\ ","\\")
        command='attrib -r -s -h "{0}" /S /D /L'.format(path)
        subprocess.call(command,shell=True)
        #print(command)
        now=datetime.now()
        dt=now.strftime("%Y/%m/%d <--> %H:%M:%S")
        history="[-] Unhide | {0} | {1}\n".format(dt,path)
        hisfile=open("his.txt","a")
        hisfile.write(history)
        hisfile.close()

def historyR():
    #chekhispass()
    if chekhispass()==1:
        his=open("his.txt","r")
        zx=his.read()
        print("\033[1;32;40m{0}".format(zx))
        his.close()
        input("\033[1;33;40m[+] Press enter to continue..")
    else:
        print("")


        
def chekhispass():
    file=open("pass.txt","r")
    file_line=file.readlines()
    if file_line[1]=="1\n":
        #sec()
        if sec()==1:
            x=1
        else:
            print("\033[1;31;40m[!] Passwd incorrect..")
            x=0
        return x;
    else:
        return 1
        





def sec():
    passwd=getpass.getpass("\033[1;33;40mpasswd>> ")
    corpasr=open("pass.txt","r")
    corpas=corpasr.readline()
    corpas=corpas.encode("ascii")
    corpas=base64.b64decode(corpas)
    corpas=corpas.decode("ascii")
    corpas=corpas
    passwd="{0}".format(passwd)
    #print("correct={0}  guess={1}".format(corpas,passwd))
    corpasr.close()
    if corpas==passwd:
        #print("correct")
        return 1
    else:
        return 0
    return x
    #print(corpas[0])

def setting():
    print("""\033[1;31;40m
    
    [+] 1.Passwd to history.
    [+] 2.Passwd to start application.
    [+] 3.Change passwd.
    
    """)
    option=input("\033[1;33;40msetting>> ")
    if option=="1":
        print("""\033[1;34;40m
    [+] 1.Set passwd
    [+] 2.Remove passwd
""")
        settpasswd=input("\033[1;33;40mHistory passwd>> ")
        if settpasswd=="1":
            file=open("pass.txt","r")
            file_line=file.readlines()
            file_line[1]="1\n"
            file.close()
            file=open("pass.txt","w")
            file.writelines(file_line)
            file.close()
            print("[+]\033[1;33;40m Setting saved sucsessful..!")
        elif settpasswd=="2":
            file=open("pass.txt","r")
            file_line=file.readlines()
            file_line[1]="0\n"
            file.close()
            file=open("pass.txt","w")
            file.writelines(file_line)
            file.close()
            print("\033[1;33;40m[+] Setting saved sucsessful..!")
    
    
    elif option=="2":
        print("""\033[1;34;40m
    [+] 1.Set passwd
    [+] 2.Remove passwd
""")
        sethispasswd=input("\033[1;33;40mApplication passwd>> ")
        if sethispasswd=="1":
            file=open("pass.txt","r")
            file_line=file.readlines()
            file_line[2]="1\n"
            file.close()
            file=open("pass.txt","w")
            file.writelines(file_line)
            file.close()
            print("\033[1;33;40m[+] Setting saved sucsessful..!")
        elif sethispasswd=="2":
            file=open("pass.txt","r")
            file_line=file.readlines()
            file_line[2]="0\n"
            file.close()
            file=open("pass.txt","w")
            file.writelines(file_line)
            file.close()
            print("\033[1;33;40m[+] Setting saved sucsessful..!")
    elif option=="3":
        passwd=getpass.getpass("\033[1;32;40m[+] Enter new passwd>> ")
        repasswd=getpass.getpass("\033[1;32;40m[+] Confirm new passwd>>")
        if passwd==repasswd:
            passwd=passwd.encode("ascii")
            passwd=base64.b64encode(passwd)
            passwd=passwd.decode("ascii")
            file=open("pass.txt","r")
            file_line=file.readlines()
            file_line[0]="{0}\n".format(passwd)
            file.close()
            file=open("pass.txt","w")
            file.writelines(file_line)
            file.close()
            print("\033[1;33;40m[+] Setting saved sucsessful..!")

if __name__=="__main__":
    main()


