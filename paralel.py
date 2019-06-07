import multiprocessing as mp
import datetime as dt
import os

def exec_print(my_param):
    print(f"PID: {os.getpid()} -> o parametro recebido é {my_param}")


def run_plain():

    i = 0
    while i < 10:
        exec_print(dt.datetime.now())
        i += 1

def run_paralel():
    pool = mp.Pool(5)
    i = 0
    while i < 10:
        pool.apply_async(exec_print, args=(dt.datetime.now(),))
        i += 1
    pool.close()
    pool.join()


if __name__ == "__main__":
    print("PLAIN:")
    run_plain()
    print("\n\n")
    print("PARALEL:")
    run_paralel()
    print("TERMINOU!")