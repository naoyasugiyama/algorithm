import random
import time


# シェルソート
# 特定の間隔(idx)でソートする
# 配列の最大値を保存しておく
# 間隔を決める (単純に分割) gap = n/2
def ShellSort(arr):
    n = len(arr)
    gap = int(n/2)
    while gap > 0:
        for i in range(gap, n):
            tmp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > tmp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = tmp
        gap = int(gap / 2)
    return arr

# シェルソートの間隔 h * 3 + 1 に変える
def ShellSrot2(arr):
    max = len(arr)
    gap = 1

    while gap < max / 9:
        gap = gap * 3 + 1
    
    while gap > 0:
        for i in range(gap, max):
            tmp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > tmp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = tmp
        gap = int( gap / 3)
    
    return arr






if __name__ == '__main__':

    '''
    アルゴリズム

    insert sortの間隔を短くしていき最終的に1にする
    間隔の設定方法によって速度がだいぶ変わる
    フィボナッチ数列もなかなか早いらしいが..

    3h + 1が速いらしい

    '''
    arr = list(range(20))
    random.shuffle(arr)
    
    t1 = time.time()
    ShellSort(arr)
    print("passage-ShellSrot:{}".format(time.time()-t1))
    print(arr) 

    arr2 = list(range(20))
    random.shuffle(arr2)

    t1 = time.time()    
    ShellSrot2(arr2)
    print("passage-ShellSrot:{}".format(time.time()-t1))
    print(arr2)




        





