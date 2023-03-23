import multiprocessing
import time
import random
import pickle


def worker_1(shared_value, shared_array, connection, lock):
    while True:
        time.sleep(random.uniform(0.5, 1.5))  # 模拟处理时间
        with lock:
            if shared_value.value >= 5:
                break
            shared_value.value += 1
            shared_array[shared_value.value - 1] = shared_value.value
            connection.send(pickle.dumps(shared_value.value))
            print(f"工作进程1：增加了值，当前值为 {shared_value.value}")


def worker_2(shared_value, shared_array, connection, lock):
    while True:
        time.sleep(random.uniform(0.5, 1.5))  # 模拟处理时间
        with lock:
            if shared_value.value >= 5:
                break
            shared_value.value += 1
            shared_array[shared_value.value - 1] = shared_value.value
            connection.send(pickle.dumps(shared_value.value))
            print(f"工作进程2：增加了值，当前值为 {shared_value.value}")


if __name__ == '__main__':
    shared_value = multiprocessing.Value('i', 0)
    shared_array = multiprocessing.Array('i', 5)

    # ⑴ 创建一个管道，并返回两个连接对象（Connection对象），通常称为parent_conn和child_conn。这两个连接对象可以用于在进程间发送和接收数据。
    parent_conn, child_conn = multiprocessing.Pipe()

    lock = multiprocessing.Lock()

    process1 = multiprocessing.Process(target=worker_1, args=(shared_value, shared_array, child_conn, lock))
    process2 = multiprocessing.Process(target=worker_2, args=(shared_value, shared_array, child_conn, lock))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    while parent_conn.poll():
        received_value = pickle.loads(parent_conn.recv())
        print(f"主进程：从管道接收到的值为 {received_value}")

    print(f"主进程：共享数组最终为 {list(shared_array)}")
