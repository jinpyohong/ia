import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Insert a row of data
c.execute("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)", 
            ('2006-01-05', 'BUY', 'RHAT', 100, 35.14))

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', '삼성전자', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# Select
c.execute('SELECT * FROM stocks')
for row in c.fetchall():
    print(row)
print()
c.execute('SELECT * FROM stocks WHERE symbol=?', ('RHAT',))
print(c.fetchone())
print()

# Updata and delete     
c.execute('UPDATE stocks SET qty=? WHERE symbol=?', (700, 'MSFT'))
c.execute('DELETE FROM stocks WHERE trans=?', ('SELL', ))

c.execute('SELECT * FROM stocks ORDER BY price')
for row in c.fetchall():
    print(row)

conn.commit()
conn.close()
