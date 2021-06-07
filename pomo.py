import time
import chime
import sys
cycle=0
t=1
def_work=25
def_free=5
def_free_long=15
while True:
    print("___________________POMODORO____________________\n\n","1. Press 1 to start the default 25 min timer\n","2. Press 2 to configure the pomodoro settings\n","3. Quit program")
    s=input()
    if(s=='1'):
        while t==1:
            if cycle==0:
                print("Press Ctrl + C to stop pomodoro")
            time.sleep(def_work*60)
            for i in range(1,4):
                chime.success()
                time.sleep(1)
            cycle=cycle+1
            if(cycle%4==0):
                time.sleep(def_free_long*60)
                for i in range(1,4):
                    chime.info()
                    time.sleep(1)
            else:
                time.sleep(def_free*60)
                for i in range(1,4):
                    chime.info()
                    time.sleep(1)
    elif(s=='2'):
        while True:
            print("\n\nSETTINGS","\n\n1. Change work duration\n2. Change the short break duration\n3. Change the long break duration\n4. Exit")
            change=input()
            if(change=='1'):
                print("Current work duration : ",time.strftime("%H:%M:%S", time.gmtime(def_work*60)))
                def_work = int(input("Enter the work duration in minutes:"))
            elif(change=='2'):
                print("Current short break : ",time.strftime("%H:%M:%S", time.gmtime(def_free*60)))
                def_free = int(input("Enter the short break duration in minutes:"))
            elif(change=='3'):
                print("Current long break : ",time.strftime("%H:%M:%S", time.gmtime(def_free_long*60)))
                def_free_long =int(input("Enter the long break duration in minutes :"))
            elif(change=='4'):
                break
            else:
                chime.warning()
                pass
    elif(s=='3'):
        sys.exit(0)
    else:
        print("Invalid command")
        chime.warning()
        pass


