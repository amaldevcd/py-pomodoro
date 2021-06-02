import time
import chime


print("___________________POMODORO____________________\n","1. Press 1 to start the default 25 min timer\n","2. Press 2 to configure the pomodoro settings\n")
s=input()
if(s=='1'):
    print("Press Ctrl + C to stop pomodoro")
    time.sleep(1500)
    for i in range(1,6):
        chime.success()
        time.sleep(1)
elif(s=='2'):
    print("\n\nSETTINGS","\n\n1. Change work duration\n2. Change the short break duration\n3. Change the long break duration")

        

