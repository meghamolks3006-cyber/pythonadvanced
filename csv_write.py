

import csv

f = open("data.csv", "w", newline="")

content = [
    ['name', 'age', 'place'],
    ['arun', 25, 'ekm'],
    ['amal', 26, 'tvm']
]

w = csv.writer(f)  # creates writer object
print(w)

w.writerows(content)  # writes each row to the file

f.close()