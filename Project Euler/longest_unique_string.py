a="abc"
b="abefa"
c="abcddddddd"

string=c

def longest_string(string):
    l=len(string)
    for x in range(l):
        left=(string[0:x+1])
        right=(string[x+1:x+2])
        if right in left:
            return x+1
            break
    
            

print(longest_string(b))

