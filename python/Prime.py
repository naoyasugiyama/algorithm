'''
1. numbers[] リターン用の配列を用意
2. 2 ~ n + 1 までの数を数える
3. フラグをtrueで初期化
4. numbers[] 配列で割り切れる数なら素数ではない (素数チェック) 
5. 割り切れる数ならそれ以上検索の必要がないのでフラグをfalseにしてbreak (余分な計算を排除)
6. 3.素数フラグを見てtrueなら numbersに追加
7. 1を配列の先頭に追加
'''
def get_prime(num):
    numbers = []
    for i in range(2, num + 1):
        flag = True
        for j in numbers:
            if i % j  == 0:
                flag = False
                break

        if flag:
            numbers.append(i)

    numbers.insert(0,1)

    return numbers 


if __name__ == '__main__':
    primes = get_prime(10000)
    print(primes)


