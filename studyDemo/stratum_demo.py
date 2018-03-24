def test_stratum(n):
    result =1
    if(n==1 or n ==0):
        return result
    for i in range(1, n+1):
        result = result*i
    return result
if __name__ == '__main__':
    print(test_stratum(8))


