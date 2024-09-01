# %% [markdown]
# ### Multiprocessing

# %%
import time
import multiprocessing
import os

# %%
def task1(msg):
    time.sleep(3)
    print(msg)
    print("Thread - Name: ", multiprocessing.current_process().name)
    print("Thread - Process Id: ", os.getpid())

def task2(msg):
    time.sleep(1)
    print(msg)
    print("Thread - Name: ", multiprocessing.current_process().name)
    print("Thread - Process Id: ", os.getpid())

# %%
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task1, args=(("Task 1",)), name="P1")
    p2 = multiprocessing.Process(target=task2, args=(("Task 2",)), name="P2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main Process - Name: ", multiprocessing.current_process().name)
    print("Main Process - Process Id: ", os.getpid())

