import time

def timed_multiplier(timer, a , b):
    st = time.time()
    time.sleep(timer)
    en = time.time()
    print(f"Time for execution {en-st}")
    return a * b

print("result:", timed_multiplier(10, 2, 3))
