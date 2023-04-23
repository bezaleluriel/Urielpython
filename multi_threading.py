import threading

# Define a global variable to be shared between threads
shared_variable = 0

# Define a function that increments the shared variable
def increment_shared_variable(lock):
    global shared_variable
    for i in range(100000):
        # Acquire the lock before accessing the shared variable
        lock.acquire()
        shared_variable += 1
        # Release the lock after accessing the shared variable
        lock.release()

# Create a lock object to be shared between threads
lock = threading.Lock()

# Create two threads that increment the shared variable
thread1 = threading.Thread(target=increment_shared_variable, args=(lock,))
thread2 = threading.Thread(target=increment_shared_variable, args=(lock,))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final value of the shared variable
print("Shared variable value:", shared_variable)
