from timer_thread import*


if __name__ == "__main__":
    #timeout ve thread in timer i degistirilebilir.
    thId_thsecond_timeout = [(1, 5, 3), (2,8,9), (3,10,5)]

    listThread = []
    for thread_id, timer, timeout_value in thId_thsecond_timeout:
        thread = TimerThread(thread_id, timer, timeout_value)
        listThread.append(thread)

    sthread(listThread)
    print("Tüm threadler tamamlandı.")
