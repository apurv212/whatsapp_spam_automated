import pyautogui
import time

a=int(input("how many")) 
b="write here the message"       #enter the mesage you want to spam in double quotation

time.sleep(5)
for i in range(a):
    pyautogui.write(b)
    pyautogui.press("enter")

print("done")

#1. In b= "write something" 
     #enter the mesage you want to spam in double quotation


#2. compile with python space  filename.py
#3. it wil ask how many times you want to spam ?
#4. lets say 20
#5. after entering, open the  target whatsapp chat within 5 sec.
                                                            
