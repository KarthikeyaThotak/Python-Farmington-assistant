#python3.7.3

import time
def stopwatch(boolean):
     global RUN
     Sec = 0
     Min = 0
     Hours = 0
     while True:
         Sec +=1
         result = "Hour: "+str(Hours)+" Minutes: "+str(Min)+" Seconds: "+str(Sec)
         print(result)
         # time.sleep(1)
         time.sleep(1)
         if Sec == 60:
             Sec = 0
             Min += 1
         
         if Min == 60:
             Sec = 0
             Min = 0
             Hours += 1
         RUN = result

stopwatch(True)
print(RUN)
