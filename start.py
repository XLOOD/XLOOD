import os
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

print("Пожалуйста подождите..")
sleep(2)
print("\nУстановка...")
sleep(2)
os.system("pkg install git -y && pkg install python -y && pkg update && pkg upgrade && git clone https://github.com/XLOOD/XLOOD.git && cd XLOOD && pip install -r install.txt && python main.cpython-310.pyc")
