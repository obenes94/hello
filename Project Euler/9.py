'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''


for a in range(1,2000):
    for b in range(a,4000):


        c=a*a+b*b
        #print(c)
        c=(c**(1/2))
        if ((a+b+c)==1000):
            print(str(a)+str(b)+str(c))
            print((a))
            print((b))
            print(c)
            print(a**2+b**2+c)
            print(a*b*c)
