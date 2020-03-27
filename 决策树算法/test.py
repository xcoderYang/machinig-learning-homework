def multiply(self, num1, num2):
    if num1 == '0' or num2 == '0':
        return '0'
    def bigAdd(add1, add2):
        radix = 0
        ans = ['0']*1000
        maxlen = max(len(add1), len(add2))
        for i in range(0, maxlen+1):
            ad1 = 0 if len(add1)<=i else int(add1[i])
            ad2 = 0 if len(add2)<=i else int(add2[i])
            sum = int(ans[i])+radix+ad1+ad2
            ans[i] = str(sum%10)
            radix = sum//10
        last = '0'
        while last == '0' and len(ans) > 0:
            last = ans.pop()
        ans.append(last)
        return ''.join(ans)
    def singleMulti(oneChar, mul1):
        radix = 0
        ans = ['0']*1000
        if oneChar == '0':
            return ['0']
        maxlen = len(mul1)
        for i in range(0, maxlen+1):
            mu1 = 0 if len(mul1) <= i else int(mul1[i])
            sum = mu1 * int(oneChar) + radix
            ans[i] = str(sum%10)
            radix = sum//10
        last = '0'
        while last == '0' and len(ans)>0:
            last = ans.pop()
        ans.append(last)
        return ans

    ans = '0'
    cloneNum1 = num1[::-1]
    cloneNum2 = num2[::-1]
    str2 = ''.join(cloneNum2)
    for i in range(0, len(cloneNum1)):
        char = cloneNum1[i]
        ans = bigAdd(ans,''.join(['0']*i+singleMulti(char, str2)))
    return ans[::-1]


print(multiply(0,"581852037460725882246068583352420736139988952640866685633288423526139","2723349969536684936041476639043426870967112972397011150925040382981287990380531232"))