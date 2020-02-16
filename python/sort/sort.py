import random 
import sys


# バブル
def BubbleSort(ary):
    max_idx = len(ary)
    for i in range(max_idx):
      for j in range( i + 1, max_idx):
        if ary[i] > ary[j]:
          ary[i],ary[j] = ary[j], ary[i]

    return ary

def BubbleSort2(ary):
  change = True
  while change:
    change = False
    for i in range(len(ary)-1):
      if ary[i] > ary[i + 1]:
        ary[i], ary[i + 1] = ary[i + 1], ary[i]
        change = True
  return ary








if __name__ == '__main__':
    # 重複無し
    l = list(range(10))
    random.shuffle(l)
    print(l)

 
    BubbleSort(l)
    print(l)

