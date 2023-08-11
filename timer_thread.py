import threading
import time


class TimerThread(threading.Thread):
    def __init__(self, thread_id, timer, timeout_value):
        super().__init__()
        self.thread_id = thread_id
        self.timer = timer
        self.timeout_value = timeout_value
        self.timeout = False


    def run(self):
        stime = time.time()
        print("Thread {} -> başladı.".format(self.thread_id))

        while True:
            etime = time.time()
            if etime - stime >= self.timer:
                break
            if etime - stime >= self.timeout_value:
                self.timeout = True
                break

        print("Thread {} -> bitti. Timeout: {}".format(self.thread_id, self.timeout))


def sthread(threads):
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
