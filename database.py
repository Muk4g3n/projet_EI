import sqlite3
import re

concord = open('concord.html', 'r', encoding='utf-8').readlines()
conn = sqlite3.connect('extraction.db')
c = conn.cursor()

c.execute('CREATE TABLE EXTRACTION (ID INTEGER, POSOLOGIE TEXT)')

content = re.findall(r"<\s*a[^>]*>(.*?)<\s*/\s*a>", str(concord))
counter = 1
for i in content:
    c.execute("""INSERT INTO EXTRACTION (ID,POSOLOGIE) VALUES(?,?);""",
              (counter, i))
    counter = counter + 1

c.execute("SELECT POSOLOGIE FROM EXTRACTION")
conn.commit()
conn.close()
