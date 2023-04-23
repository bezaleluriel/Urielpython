from multiprocessing import Process, Pipe

def send_msgs(conn, msgs):
    for msg in msgs:
        conn.send(msg)
    conn.close()

if __name__ == '__main__':
    # Create a pipe
    parent_conn, child_conn = Pipe()

    # Create a process that sends messages through the pipe
    p = Process(target=send_msgs, args=(child_conn, ['msg1', 'msg2', 'msg3']))

    # Start the process
    p.start()

    # Receive messages from the pipe
    while True:
        try:
            msg = parent_conn.recv()
            print(f"Received message: {msg}")
        except EOFError:
            break

    # Wait for the process to finish
    p.join()
