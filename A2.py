def is_prime(nums):
    for n in nums:
        for i in range (2,int(n**0.5)+1):
            if i==n:
                continue
            if n%i==0:
                nums.remove(n)
                break
    return nums

l=[4,5,6,7,11,12]
ans=is_prime(l)
result=[x**2 for x in ans]
print(result)