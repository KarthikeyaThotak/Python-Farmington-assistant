import time

def stopwatch(sec):
    mins = sec // 60
    sec = sec % 60 
    hours = mins // 60
    mins = mins % 60
    result = "It has been "+str(hours)+" minutes "+str(mins)+" seconds "+str(sec)
    return result

def start():
    start_time = time.time()
    return start_time

def end():
    end_time = time.time()
    return end_time

def time():
    time_lapsed = start()-end()
    return time_lapsed
start()
sleep(60)
stop()
time()
stopwatch(time_lapsed)

