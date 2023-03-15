"""
定义有自动管理资源的类
"""


class MyContentMgr(object):
    def __enter__(self):
        print("enter方法被调用执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被调用执行了")

    def show(self):
        print("show方法被调用执行了")


with MyContentMgr() as file:
    file.show()
