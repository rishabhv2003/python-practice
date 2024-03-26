import time

def cal_timer(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        func(*args, **kwargs)
        en = time.time()
        print(f"Name of the function: {func.__name__} Time for execution {en-st}")
    return wrapper

@cal_timer
def timed_multiplier(timer, a , b):
    time.sleep(timer)
    return a * b

print("result:", timed_multiplier(10, 2, 3))