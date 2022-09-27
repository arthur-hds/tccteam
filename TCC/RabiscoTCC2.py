# import arrow
from time import sleep
import os
import subprocess
from xvfbwrapper import Xvfb


pasta = os.getcwd()+'\RabiscoTCC.exe'
print(pasta)
# subprocess.run('where python', shell=True, text=True)


rotina = subprocess.run(f'schtasks /create /tn testeCMDbanana /tr "{pasta}" /sc once /st 11:00', shell=True, text=True)