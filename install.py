from subprocess import call, Popen, PIPE
true = [True, "si", "Si", "s", "S", 1, "Yes", "yes", "Y", "y", "true"]
res = input("¿Usas sudo? (y/n)")
sudo = False
user = ""
if res in true:
    sudo = True

auxHome = Popen("echo $HOME", shell=True, stdout=PIPE,  stderr=PIPE)
home =   auxHome.communicate()
home = home[0].rstrip()



call(["wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'"], shell = True)

call([" /home/zykor/"], shell = True)
call(["pwd"], shell = True)


#wget 'http://nginx.org/download/nginx-1.7.2.tar.gz'