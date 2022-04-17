'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

#print(5*7*13*29)

a=600851475143

'''for x in range (1,13):
    for y in range (1,x):
        if x%y!=0 and x!=y:

            break

    else:
        print(x)
'''

#while True:
for y in range (1,10000):
        if a%y==0:
            a=a/y
            print(y)


print(6857*1471*839*71)