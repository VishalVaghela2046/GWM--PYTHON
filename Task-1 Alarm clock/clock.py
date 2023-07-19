from playsound import playsound
import time
import os
 
 
CLEAR_AND_RETURN="\033[H"

def alarm(secs) :
    time_Elapsed=-1
    os.system('cls')
    
    while time_Elapsed <secs:
        time.sleep(1)
        time_Elapsed += 1
        
        time_to = secs - time_Elapsed
        minutes_left=time_to//60
        seconds_left=time_to%60
        
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    playsound(r"E:\Downloads\ring2-mp3-6551.mp3")
    
 
alarm(10)
