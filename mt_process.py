from multiprocessing import Process, Queue

def work(start, end, result):
    total = 0
    for i in range(start, end):
        total +=1 
        print("@@@@@@@@@@@@@@@@@@@")
    result.put(total)
    return

def work2(start, end, result):
    total = 0
    for i in range(start, end):
        total +=1 
        print("===================")
    result.put(total)
    return

if __name__ == "__main__":
    START, END = 0, 100
    result = Queue()
    pr1 = Process(target = work , args =(START,END//2, result))
    pr2 = Process(target = work2 , args =(END//2,END, result))

    pr1.start()
    pr2.start()

    pr1.join()
    pr2.join()

    result.put("STOP")
    total = 0
    while 1:
        temp = result.get()
        if temp == 'STOP':
            break
        else:
            total += temp

    print(f"Result:{total}")


# 파이썬에서 병렬성을 얻고싶으면 멀티 프로세싱, GPU , 분산처리 등을 할수있는데
# 이떄 멀티 프로세싱은 쓰레드와 거의 비슷하다