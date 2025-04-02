def frequency(number):
    ans = {}
    for i in number:
        if i in ans:
            ans[i] +=1
        else:
            ans[i] = 1
    return ans
number = 1,56,789,789,7,7
print(frequency(number))