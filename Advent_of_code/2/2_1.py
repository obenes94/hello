import re

measurements=[]

with open('2/input.txt') as f:       
    for line in f:        
        measurements.append(line.strip().split())

forward=0
up=0
down=0

for i in range (len(measurements)):
    if measurements[i][0]=="forward":
        forward= forward + int(measurements[i][1])
    elif measurements[i][0]=="up":
        up= up + int(measurements[i][1])
    elif measurements[i][0]=="down":
        down= down + int(measurements[i][1])

result= (down-up)*forward

print(result)