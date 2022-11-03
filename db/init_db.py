import sqlite3

conn = sqlite3.connect('receipts.db')
cur = conn.cursor()




#"name": "PURINA ONE Корм д/кош стерил кур/зел фас 75г ",
#"price": 3099,
#"quantity": 4,
#"sum": 12396

cur.execute("""CREATE TABLE IF NOT EXISTS losts(
    category TEXT,
    name TEXT,
    date DATE,
    sum INT);
""")
conn.commit()


cur.execute("""CREATE TABLE IF NOT EXISTS income(
   name TEXT,
   date DATE,
   sum INT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS savings (
   name TEXT,
   date DATE,
   sum INT);
""")
conn.commit()
