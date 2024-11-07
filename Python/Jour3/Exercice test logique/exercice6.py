def premier (x,y):
    result = []
    for n in range(x,y + 1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break
            else:
                result.append(n)
    print(result)

premier(10, 50)

premier(1, 20)

premier(50, 70)