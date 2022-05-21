from multiprocessing import Process, Manager


def f(msg, lock):
    for key, value in msg.items():
        lock.acquire()
        print(key, value)
        for _ in range(len(msg[key])):
            msg[key].pop(0)
        lock.release()
        # for i in msg[key]:
        #     if len(i) > 0:
        #         i.pop(0)
        #     else:
        #         break
    for key, value in msg.items():
        lock.acquire()
        print(key, value)
        lock.release()


if __name__ == '__main__':
    manager = Manager()
    lock = Manager().Lock()

    msg = manager.dict()
    l = ['a', 'b', 'c']
    for i in l:
        msg[i] = manager.list([1, 2, 3])

    p1 = Process(target=f, args=(msg, lock,))
    # p2 = Process(target=f, args=(msg,lock,))
    # p3 = Process(target=f, args=(msg,lock,))

    p1.start()
    # p2.start()
    # p3.start()
    p1.join()
    # p2.join()
    # p3.join()

    # for d in msg:
    #     print(str(d))
