import threading
from concurrent.futures import ThreadPoolExecutor
import time
import logging
import random

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


# 定义要在线程中运行的函数
def worker(semaphore, thread_local_data):
    # 获取线程局部变量
    my_data = thread_local_data.data
    logging.info(f'线程 {my_data} 开始执行')

    with semaphore:
        logging.info(f'线程 {my_data} 获取到了信号量')
        time.sleep(random.uniform(1, 3))  # 模拟处理过程
        logging.info(f'线程 {my_data} 释放了信号量')

    logging.info(f'线程 {my_data} 完成')


# 初始化线程局部存储
thread_local = threading.local()

# 创建一个信号量，允许最多2个线程同时访问
semaphore = threading.Semaphore(2)

# 创建一个线程池
pool_size = 4
with ThreadPoolExecutor(pool_size) as executor:
    futures = []
    for i in range(pool_size):
        thread_local.data = i  # 为每个线程分配局部变量
        future = executor.submit(worker, semaphore, thread_local)
        futures.append(future)

    # 等待所有任务完成
    for future in futures:
        future.result()

logging.info('所有线程已完成')
