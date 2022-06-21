measurements=[]

with open('1/input.txt') as f:
    for line in f:        
        measurements.append(int(line.strip()))



x=0

for i in range (len(measurements)):
    try:
        if ((measurements[i] + measurements[i+1] + measurements[i+2])-(measurements[i+1] + measurements[i+2] + measurements[i+3]))<0:
            x=x+1
    except (IndexError):
        pass

print(x)