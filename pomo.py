import time
import chime


print("___________________POMODORO____________________\n","1. Press 1 to start the default 25 min timer\n","2. Press two to configure the pomodoro settings\n")
s=input()
if(s.lower()=="start"):
    print("Press Ctrl + C to stop pomodoro")
    time.sleep(1500)
    for i in range(1,6):
        chime.success()
        time.sleep(1)
        

