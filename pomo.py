import time
import chime
cycle=0
t=1
def_work=1500
def_free=300
def_free_long=1200

print("___________________POMODORO____________________\n","1. Press 1 to start the default 25 min timer\n","2. Press 2 to configure the pomodoro settings\n")
s=input()
if(s=='1'):
    while t==1:
        print("Press Ctrl + C to stop pomodoro")
        time.sleep(10)
        for i in range(1,6):
            chime.success()
            time.sleep(1)
        cycle=cycle+1
        if(cycle%4==0):
            time.sleep(6)
            for i in range(1,4):
                chime.info()
                time.sleep(1)
        else:
            time.sleep(3)
            for i in range(1,4):
                chime.warning()
                time.sleep(1)
elif(s=='2'):
    print("\n\nSETTINGS","\n\n1. Change work duration\n2. Change the short break duration\n3. Change the long break duration")


        

