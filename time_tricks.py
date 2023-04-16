import multiprocessing
import time

def sleepy_man(id):
    print(f'Starting to sleep with id: {id}')
    time.sleep(1)
    print(f'Done sleeping with id: {id}')


def f1(x):
    return x**2
# the main is to make sure that the new process will not execute this code.
# because the multiprocessing.Process(target=sleepy_man) import this file in another interpeter and execute it
if __name__ == "__main__":
    ###########################################################################
    print(multiprocessing.cpu_count())
    tic = time.time()
    # each process run on different core in parallel
    list_of_proc = [multiprocessing.Process(target=sleepy_man, args=(i,)) for i in range(1,5)]
    for i in list_of_proc:
        i.start()
    # join wait for finish
    for i in list_of_proc:
        i.join()
    toc = time.time()
    # we can see in print that all of them worked in parallel on multiple cores.. the time is 1 second approx
    print('Done in {:.4f} seconds'.format(toc - tic))
    ###########################################################################
    # example to run some function on all cores in computer dynimically
    numbers = list(range(1,11))
    my_pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    my_list = my_pool.map(f1, numbers)
    print(my_list)
