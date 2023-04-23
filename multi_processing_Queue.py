from multiprocessing import Process, Queue

def send_msgs(q, msgs):
    for msg in msgs:
        q.put(msg)

if __name__ == '__main__':
    # Create a queue
    q = Queue()

    # Create a process that sends messages through the queue
    p = Process(target=send_msgs, args=(q, ['msg1', 'msg2', 'msg3']))

    # Start the process
    p.start()

    # Receive messages from the queue
    while not q.empty():
        msg = q.get()
        print(f"Received message: {msg}")

    # Wait for the process to finish
    p.join()
