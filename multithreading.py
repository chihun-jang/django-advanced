from threading import Thread

def work(start,end,result):
    total = 0
    for i in range(start, end):
        total += 1
        print("워후",i)
    result.append(total)

    return

def work2(start,end,result):
    total = 0
    for i in range(start, end):
        total += 1
        print("=================",i)
    result.append(total)

    return

if __name__ == "__main__":

    START, END = 0, 100
    result = list()
    th1 =Thread(target=work , args=(START, END//2, result))
    th2 = Thread(target=work2, args=(END//2, END, result))
    th1.start()
    th2.start()

    th1.join()
    th2.join()
print(f"Result:{sum(result)}")

# # 
# 일반적으로는 멀티 쓰레딩이 멀티 프로세싱 보다 효율적이다. 멀티 프로세싱을 위해서 프로세스를 더 생성하게 되면 생성되는 프로세스는 기존에 프로세스가 가지는 데이터와 공간을 똑같이 복사하여 가지게 된다. 반면에 쓰레드는 프로세스의 공간 및 자원을 다른 쓰레드와 공유하고 스택만을 따로 가지기때문에 생성되는 시간이 짧으며, 컨텍스트 스위칭이 일어날 때도 프로세스에 비해 오버헤드가 적게 발생한다.

# 하지만 파이썬에서는 GIL(Global Interpreter Lock)으로 인해 멀티 쓰레딩을 하더라도 싱글 쓰레드보다 속도면에서 이점을 가지기 힘들다. GIL은 자원의 보호를 위해 파이썬 프로그램이 실행될 때 여러개의 쓰레드가 실행되더라도 한번에 하나의 쓰레드만 실행되도록 한다.
# 따라서 연산을 멀티 쓰레딩으로 구현해도 성능향상을 기대할수는 없다.
# (I/O, 비동기에서는 활용가능)

