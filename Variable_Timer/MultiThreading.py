# from multiprocessing import Process
import concurrent.futures
import time

start = time.perf_counter()
def do_something(time_for_sleep):
    print(f'Sleeping {time_for_sleep} second...')
    time.sleep(time_for_sleep)
    return f'Done Sleeping...{time_for_sleep}'

with concurrent.futures.ProcessPoolExecutor() as executor:

    if __name__ == '__main__':
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something,secs)

        for result in results:
            print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2 )} second(s)')



