


primenumbers=[]
a=1
b=2
while a<2000000:
    a=a+1
    for y in range (b,a):
            if a%(y)==0:

                b=2

                break
    else:
        primenumbers.append(a)
        print(a)

print(sum(primenumbers))