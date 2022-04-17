'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

for x in range (0,240000000,20):
    for y in range(1,21):
        if x%y!=0:
            break
    else:
        print(x)


#Not an ideal solution!