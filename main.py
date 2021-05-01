from multiprocessing import Process, Queue
import random

def element(index, A, B, queue):
    i, j = index
    res = 0
    N = len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    queue.put(res)
    return res

def new_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(1, 100))
    return matrix

queue = Queue()
res = []
n = int(input("Размерность : "))
if (n > 1):
    matrix1 = new_matrix(n)
    print(matrix1)
    matrix2 = new_matrix(n)
    print(matrix2)
for i in range(0, n):
    tmp = []
    for j in range(0, n):
        process = Process(target=element, args=[(i, j), matrix1, matrix2, queue])
        process.start()
        process.join()
        tmp.append(queue.get())
    res.append(tmp)
print(res)
queue.close()
queue.join_thread()