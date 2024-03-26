import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer 
def example(n):
    time.sleep(n)
    
# thsi declaration is same as the above declaration of decorator
# example = timer(example)
    
example(2)