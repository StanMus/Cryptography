
Par = 1
# from module1 import *

class A():
    def fun(self):
        self.ttt=1

    def fu(self):
        self.xxx = 1



def main():
    a = A()
    print(dir(a))
    # print(a.fu())


if __name__ == '__main__':
    main()