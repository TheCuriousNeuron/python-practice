def FizzBuzz(n,k):
    for i in range(1,n+1):
        flag=False
        if i%3==0:
            print("Fizz",end='')
            flag=True
        if i%5==0:
            print("Buzz",end='')
            flag=True
        if i%k==0:
            print("Boom",end='')
            flag=True
        if not flag:
            print(i,end='')
        print()

n=int(input("Enter n: "))
k=int(input("Enter k: "))

FizzBuzz(n,k)