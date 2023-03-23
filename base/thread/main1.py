import multiprocessing


def worker(child_conn):
    data = child_conn.recv()  # 从管道接收数据
    print(f"工作进程接收到数据：{data}")


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    process = multiprocessing.Process(target=worker, args=(child_conn,))
    process.start()

    parent_conn.send("来自主进程的消息1")  # 向管道发送数据
    parent_conn.send("来自主进程的消息2")  # 向管道发送数据

    response1 = parent_conn.recv()  # 从管道接收数据
    print(f"主进程接收到消息：{response1}")

    process.join()
