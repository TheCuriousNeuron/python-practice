def FizzBuzz(n,k):
    ans=[]
    for i in range(1,n+1):
        entry=''
        # flag=False
        if i%3==0:
            # print("Fizz",end='')
            entry+='Fizz'
            # flag=True
        if i%5==0:
            # print("Buzz",end='')
            entry+='Buzz'
            # flag=True
        if i%k==0:
            # print("Boom",end='')
            entry+='Boom'
            # flag=True
        if entry=='':
            # print(i,end='')
            entry=str(i)
        ans.append(entry)
    return ans

# n=int(input("Enter n: "))
# k=int(input("Enter k: "))

# FizzBuzz(n,k)