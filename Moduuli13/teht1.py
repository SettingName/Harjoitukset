def isPrime(checkNum: int):
    totalDiv = 0
    for num in range(1, checkNum + 1):
        if checkNum % num == 0:
            totalDiv += 1
    if totalDiv == 2:
        return True
    else:
        return False