import bisect
import random
import sys

sys.setrecursionlimit(10 ** 5)


# バイナリサーチ
def binSearch(ary, low, high, val):
    if low == high:
      if ary[low]  > val:
        return low
      else:
        return low + 1
    elif low > high:
      return low

    mid = (low + high) // 2
    if ary[mid] < val:
      return binSearch(ary, mid + 1, high, val)
    elif ary[mid] > val:
      return binSearch(ary, low, mid - 1, val )
    else:
      return mid

# バイナリサーチ版
def InsertSort2(ary):
    for i in range(1, len(ary)):
      val = ary[i]
      idx = binSearch(ary, 0, i - 1, val)
      ary[:] = ary[:idx] + [val] + ary[idx:i] + ary[i + 1:]
    else:
      return ary

# bisect版 配列二分法アルゴリズム  github:https://github.com/python/cpython/blob/3.8/Lib/bisect.py
def InserSort3(ary):
    for i in range(1, len(ary)):
        bisect.insort(ary, ary.pop(i), 0, i)
    else:
      return ary


if __name__ == '__main__':
    # 重複無し
    l = list(range(1000))
    random.shuffle(l)
    print(l)

