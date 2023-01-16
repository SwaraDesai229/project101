# import the time module 
import time 
seconds=input("enter the number of seconds ")


# define count down timer function
def countdown_timer(seconds):
    
   while seconds:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer,end='\r')
        time.sleep(1)
        seconds-=1
    print("time Up")
  
#function call 
countdown_timer(int(seconds))
