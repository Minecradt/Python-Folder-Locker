import os,hashlib
from base64 import urlsafe_b64encode,encode,decode,urlsafe_b64decode
sys = os.system
sys('pip install pyAesCrypt > nul 2>nul')
sys("color 2")
import pyAesCrypt
exist = os.path.isdir
bufferSize = 64 * 1024
try:
    os.mkdir("procldta")
except:
    pass
if not exist('procldta\\P__NPL'):
    try:
        os.mkdir("procldta\\Locker")
    except:
        pass
try:
    f = open("procldta\\dat.ini", 'x')
    f.close()
except:
    pass

direct = os.path.split(__file__)[0] + "\\procldta"







#Folder Unlocking
def UnlockFolder():
    from glob import glob
    from pathlib import Path
    import os
    #print(direct)
    os.mkdir(direct + '\\tmp')
    os.rename(direct + '\\P__NPL',direct+'\\tmp\\Locker')
    p = Path(direct + '\\tmp').glob('**/*')
    out = list(p)
    #print(out)
    for i in (out):
        path = i
        try:
            os.listdir(path)
        except:
            pass
            #print('Error!')
            #print(path)
        else:
            for files in os.listdir(path):
                if os.path.isfile(os.path.join(path, files)):
                    filename = os.path.join(path, files)
                    #print(filename)
                    try:
                        skip = 1
                    except:
                        continue
                    else:
                        try:
                            skip = 1
                        except:
                            continue
                        else:
                            newname = urlsafe_b64decode(bytes(os.path.splitext(files)[0].encode('utf-8'))) + b'.' + urlsafe_b64decode(bytes(os.path.splitext(files)[1][::-1][:-1][::-1].encode('utf-8')))
                            #print(newname)
                            writepath = os.path.join(path,newname.decode('utf-8'))
                            print('Decrypting: '+filename)
                            repeat = divide%4
                            decode(open(filename,'rb'),open(writepath,'wb'))
                            os.unlink(filename)
                            for i in range(repeat):
                                decode(open(writepath,'rb'),open(writepath+'.1','wb'))
                                os.unlink(writepath)
                                os.rename(writepath + '.1',os.path.splitext(writepath + '.1')[0])
    os.rename(direct + '\\tmp\\Locker',direct + '\\Locker')
    os.rmdir(direct + '\\tmp')








#Folder Locking
def LockFolder():
    from glob import glob
    from pathlib import Path
    import os
    #print(direct + '\\Locker','P__NPL')
    os.mkdir(direct + "\\tmp")
    os.rename(direct + '\\Locker',direct + '\\tmp\\P__NPL')
    p = Path(direct + "\\tmp").glob('**/*')
    out = list(p)
    #print(out)
    for i in (out):
        path = i
        try:
            os.listdir(path)
        except:
            pass
            #print('Error!')
            #print(path)
        else:
            for files in os.listdir(path):
                if os.path.isfile(os.path.join(path, files)):
                    filename = os.path.join(path, files)
                    #print(filename)
                    try:
                        skip = 1
                    except:
                        continue
                    else:
                        try:
                            skip = 1
                        except:
                            continue
                        else:
                            newname = urlsafe_b64encode(bytes(os.path.splitext(files)[0].encode('utf-8'))) + b'.' + urlsafe_b64encode(bytes(os.path.splitext(files)[1][::-1][:-1][::-1].encode('utf-8')))
                            writepath = os.path.join(path,newname.decode('utf-8'))
                            print('Encrypting: ' + filename)
                            repeat = (divide%4)
                            encode(open(filename,'rb'),open(writepath,'wb'))
                            os.unlink(filename)
                            for i in range(repeat):
                                encode(open(writepath,'rb'),open(writepath + '.1','wb'))
                                os.unlink(writepath)
                                os.rename(writepath + '.1',os.path.splitext(writepath + '.1')[0])
    os.rename(direct + '\\tmp\\P__NPL',direct + '\\P__NPL')
    os.rmdir(direct + '\\tmp')


def CalculateTimes():
    global divide
    
    with open("procldta\dat.ini", 'r') as f:
        lock = f.readlines()
    f.close()
    lock = ''.join(lock)
    lock = lock.split("\n")
    lock = lock[0]
    interger = int(lock,16)
    divide = 1
    for i in str(interger):
        if i=='0':
            i = 9
        else:
            i = int(i)
        divide = divide*i
    for i in str(interger):
        if i=='0':
            i = 9
        else:
            i = int(i)
        divide = divide-i
        divide = divide-i
    
    #print(divide)
#print(lock)
#exit()
with open('procldta/dat.ini','r') as f:
    hashed = f.readlines()
f.close()
if not hashed==[]:
    CalculateTimes()
def HandlePassword(password):
    hashed = hashlib.shake_256(password.encode('utf-8')).hexdigest(256)
    with open('procldta\dat.ini','w') as wr:
        wr.write(hashed)
    wr.close()
#CalculateTimes()
#UnlockFolder()
def lockui():
    sys("cls")
    if exist(f'{direct}\\P__NPL'):
        print('1: Unlock Folder')
        unlock = True
    else:
        print('1: Lock Folder')
        unlock = False
    print("2: Change password")
    print("3: Exit Locker")
    try:
        ans = int(input())
    except:
        print("Enter Number!")
        lockui()
        exit()
    else:
        if ans > 3 or ans < 1:
            print("Not Valid Option")
            lockui()
            exit()
    if ans==2:
        with open('procldta/dat.ini','r') as f:
            test = f.readlines()
        f.close()
        if test==[]:
            password = input('What Password Do You Want: ')
        else:
            passwordchk = input("What is your password: ")
            passwordchk = hashlib.shake_256(passwordchk.encode('utf-8')).hexdigest(256)
            if passwordchk==''.join(test):
                password = input('What Password Do You Want: ')
            else:
                lockui()
                exit()
        HandlePassword(password)
        if unlock==True:
            UnlockFolder()
        CalculateTimes()
        if unlock==True:
            LockFolder()
    elif ans==1 and unlock == True:
        with open('procldta/dat.ini','r') as f:
            test = f.readlines()
        f.close()
        if test==[]:
           print('Please Set A Password')
           input()
           lockui()
           exit()
        else:
            password = input("What is your password: ")
            passwordchk = hashlib.shake_256(password.encode('utf-8')).hexdigest(256)
            if passwordchk==''.join(test):
                print('Make sure nothing is accessing the folder/files otherwise the DECRYPTION process will not work!!!!!!!!\nPress Any Key to start process!')
                sys('pause > nul')
                UnlockFolder()
                del password
    elif ans==1:
        with open('procldta/dat.ini','r') as f:
            test = f.readlines()
        f.close()
        if test==[]:
           print('Please Set A Password')
           input()
           lockui()
           exit()
        print('Make sure nothing is accessing the folder/files otherwise the ENCRYPTION process will not work!!!!!!!!\nPress Any Key to start process!')
        sys('pause > nul')
        LockFolder()
    else:
        exit()
    lockui()
    exit()
lockui()
