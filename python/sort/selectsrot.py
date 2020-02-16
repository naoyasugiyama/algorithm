import random


# 選択ソート
def SelectSort1(ary):
    max = len(ary)
    for i in range(0, max - 1):
      min = i
      for j in range( i + 1, max):
        if ary[min] > ary[j]:
          min = j
      else:
        ary[min],ary[i] = ary[i],ary[min]

def SelectSort2(ary):
  for idx, val in enumerate(ary):
    min_idx = min(range(idx, len(ary)), key=ary.__getitem__)
    ary[idx], ary[min_idx] = ary[min_idx], val
  return ary


if __name__ == '__main__':
    # 重複無し
    l = list(range(10))
    random.shuffle(l)
    print(l)

