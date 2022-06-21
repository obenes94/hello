"""import requests

url = 'https://adventofcode.com/2021/day/1/input'
r = requests.get(url, allow_redirects=True)

open('input', 'wb').write(r.content)"""

measurements=[]

with open('1/input.txt') as f:
    for line in f:        
        measurements.append(int(line.strip()))



x=0

for i in range (len(measurements)):
    try:
        if (measurements[i]-measurements[i+1])<0:
            x=x+1
    except (IndexError):
        pass

print(x)

