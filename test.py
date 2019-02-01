import collections

def my_queue(n=5):
    mylist = collections.deque(maxlen=n)
    
    return [-1:]

# my_queue(n=5)
if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))