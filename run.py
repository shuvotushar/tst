import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
def o():
    os.system('clear')
    print(logo)
    print(" \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××")
    jalan(" \033[38;5;196m[\033[38;5;195mA\033[38;5;196m]\033[38;5;195m NOT \033[1;91m[\033[1;97mWORKING\033[1;91m]")
    print(" \033[38;5;196m[\033[38;5;195mB\033[38;5;196m]\033[38;5;195m MY FB ACCOUNT")
    print(" \033[38;5;196m[\033[38;5;195mC\033[38;5;196m]\033[38;5;195m MY FB GROUP")
    print(" \033[38;5;196m[\033[38;5;195mD\033[38;5;196m]\033[38;5;195m TAKLA ACCOUNT")
    print(" \033[38;5;196m[\033[38;5;195mE\033[38;5;196m]\033[38;5;195m TAKLA ACCOUNT 2")
    print(" \033[38;5;196m[\033[38;5;195mF\033[38;5;196m]\033[38;5;195m EXIT")
    print(" \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××")
    SHUVO  = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;45m Choice Option \033[38;5;196m: ')
    if SHUVO  == 'A':
        hasan ()
    if SHUVO  == 'B':
        os.system('xdg-open https://www.facebook.com/shuvo.2k3?mibextid=ZbWKwL')
        return None
    if SHUVO  == 'C':
        os.system('xdg-open fb://group/720995922656547?ref=share&mibextid=NSMWBT')
        return None
    if SHUVO  == 'D':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100048248107348&mibextid=ZbWKwL')
        return None
    if SHUVO  == 'E':
    	os.system('xdg-open https://www.facebook.com/profile.php?id=100076167770204&mibextid=ZbWKwL')
        return None
    if SHUVO  == 'F':
        os.system('exit')
        return None
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;196mSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \033[38;5;196m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;196m Sorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \033[38;5;196m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""
  \033[38;5;46m ███████ ██   ██ ██    ██ ██    ██  ██████ 
  \033[38;5;46m ██      ██   ██ ██    ██ ██    ██ ██    ██ 
  \033[38;5;46m ███████ ███████ ██    ██ ██    ██ ██    ██ 
  \033[38;5;46m      ██ ██   ██ ██    ██  ██  ██  ██    ██ 
  \033[38;5;46m ███████ ██   ██  ██████    ████    ██████
         
 \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mCREATED BY\033[38;5;196m   :  \033[38;5;195mABDUL KADER SHUVO    \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mFACEBOK      \033[38;5;196m: \033[38;5;195mABDUL KADER SHUVO                 \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mGITHUB       \033[38;5;196m:  \033[38;5;195mshuvotushar                \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mTOOL STATUS  \033[38;5;196m: \033[38;5;195m takla dst tst             \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mTEAM         \033[38;5;196m:  \033[38;5;195mganja-khor                 \033[38;5;46m|
 \033[38;5;46m|     \033[38;5;196m[\033[38;5;45m✓\033[38;5;196m] \033[38;5;195mTOOL VIRSION \033[38;5;196m:  \033[38;5;195mganja-khor-pro                   \033[38;5;46m|
 \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××
 \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m PLZ SAPPORT ME BRO....
 \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m TAKLA MURAD KHOR
 \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××""")
def linex():
	print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
 
o()
 r 
