import threading
import time

# Function to run in thread
def print_numbers():
    for i in range(1, 6):
        print(f" T1 : {i}")
        time.sleep(3)

def print_numbers2():
    for i in range(1, 6):
        print(f" T2 : {i}")
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers2)

# Starting threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Both threads have finished.")
