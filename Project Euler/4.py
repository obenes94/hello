'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

numbers=[]

for x in range(100,999):
    for z in range(100,999):
        y=int(z*x)
        part1=str(y)[0:3:1]
        part2=str(y)[3:6:1]
        part2op=part2[::-1]
        if(part1==part2op):
            print(str(z) + '*' + str(x))
            numbers.append(y)
palindrome=max(numbers)
print(str(palindrome))
   



