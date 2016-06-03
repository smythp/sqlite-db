import sqlite3
import csv

with open('file','r') as file:
    text = file.readlines()

l = csv.reader(text)

for item in l:
    headers = item
    break

#print(headers)    

ids = [2, 4, 5, 8, 9, 10, 11, 16, 17, 29, 30, 38]

new_headers = []

for i, item in enumerate(headers):
    if i in ids:
        new_headers.append(item)

#print(new_headers)        
        
    

conn = sqlite3.connect('db.db')
cur = conn.cursor()



new_headers = tuple(new_headers)

#print(new_headers)
#print(len(new_headers))

query = "CREATE TABLE item (id integer primary key, %s text, %s text, %s text, %s text, %s text, %s text, %s text, %s text, %s text, %s text, %s text, %s text);" % new_headers

cur.execute(query)

l = list(l)



for row in l[1:]:
    new_row = []
    for i, field in enumerate(row):
        if i in ids:
            new_row.append(field)
    new_row = [None] + new_row
    t = tuple(new_row)
#    print(len(t))
    print(t)
    cur.execute("INSERT INTO item VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", t)
conn.commit()

