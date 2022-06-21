measurements=[]

with open('2/input.txt') as f:       
    for line in f:        
        measurements.append(line.strip().split())

forward=0
aim=0
depth=0

for i in range (len(measurements)):
    if measurements[i][0]=="forward":
        forward= forward + int(measurements[i][1])
        depth=depth+aim * int(measurements[i][1])
    elif measurements[i][0]=="up":
        aim= aim - int(measurements[i][1])
    elif measurements[i][0]=="down":
        aim= aim + int(measurements[i][1])

result= depth*forward

print(result)