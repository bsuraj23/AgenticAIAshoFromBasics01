import threading

def task():
    print("Thread has started!" *3)
    print("Thread has started!" *3)
    print("Thread has started!" *3)




# Create and start the thread
my_thread = threading.Thread(target=task)
  # Starts running in parallel
my_thread.start()
