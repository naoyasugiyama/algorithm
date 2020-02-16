import random

# 挿入ソート
def InsertSort(ary):
  for i in range(1 ,len(ary)):
    key = ary[i]
    j = i - 1
    while j >= 0 and key < ary[j]:
      ary[j + 1] = ary[j]
      j -= 1
    ary[j+1] = key 

  return ary


if __name__ == '__main__':
    # 重複無し
    l = list(range(10))
    random.shuffle(l)
    print(l)

    # 挿入ソート
#    InsertSort(l)
    InsertSort(l)

    print(l)
    #print(l)


