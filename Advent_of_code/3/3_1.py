bites=[]
#read text, create eneough lists and fill them with values
with open('3/input.txt') as f:
    firstline = f.readline()
    for i in range(len(firstline.strip())):
        bites.append([]) 
     
    for line in f:
        for i in range(len(line.strip())):        
            bites[i].append(line.strip()[i])


def power_consumption(bites):
    gamma=''
    epsilon=''
    for i in range(len(bites)):
        if bites[i].count('1')<bites[i].count('0'):
            gamma=gamma+'0'
            epsilon=epsilon+'1'
        else:
            gamma=gamma+'1'
            epsilon=epsilon+'0'

    gamma=int(gamma, 2)
    epsilon=int(epsilon, 2)

    result=gamma*epsilon
    return result

print(power_consumption(bites))


