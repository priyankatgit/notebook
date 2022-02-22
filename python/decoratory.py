import time
def time_logger(func):

    def func_executor(*args, **kwrargs):
        start_time = time.time()

        result = func(*args, **kwrargs)
        
        end_time = time.time()
        print("Taken time in seconds:", end_time - start_time)
        return result
    
    return func_executor


@time_logger
def long_running_fn(length):
    for i in range(length):
        print(i)
    return "done"

print(long_running_fn(10, 20))