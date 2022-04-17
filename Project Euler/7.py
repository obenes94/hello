'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''


primenumbers=[]
a=1
b=2
while (len(primenumbers))<10001:
    a=a+1
    for y in range (b,a):
            if a%(y)==0:

                b=2

                break
    else:
        primenumbers.append(a)
        print(a)

print(len(primenumbers))







