from pathlib import Path

p1=Path('data.csv')

with open(p1,'r') as file:
    print(file.read())