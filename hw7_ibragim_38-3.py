import sqlite3

db = sqlite3.connect('studentss.db')
c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS  student(
hobby text,
name text,
surname text,
data_dr,
points_ds
) ''')


c.execute('''INSERT INTO student VALUES ('drawing', 'ibragim', 'ahunbavaev', 2009, 8)''')
c.execute('''INSERT INTO student VALUES ('dance','altynai','pamirbekova',2011,9)''')
c.execute('''INSERT INTO student VALUES ('gaming','taku','mirbolotov',2006,10)''')
c.execute('''INSERT INTO student VALUES ('football','arlen','kayrbekov',2008,15)''')
c.execute('''INSERT INTO student VALUES ('reading','adelina','kaparbaeva',2009,13)''')
c.execute('''INSERT INTO student VALUES ('sing','janylai','kamchibaeva',2004,11)''')
c.execute('''INSERT INTO student VALUES ('voleiball','bilal','ismailov',2010,7)''')
c.execute('''INSERT INTO student VALUES ('basketball','ramil','belekov',2006,7)''')
c.execute('''INSERT INTO student VALUES ('run','doni','baltabaev',2009,17)''')
c.execute('''INSERT INTO student VALUES ('tennis','abu','abduseitov',2005,13)''')

c.execute('''SELECT name FROM student WHERE surname > 10''')

c.execute("""UPDATE student SET name == 'genius' WHERE points_ds >= 10""")
print(c.fetchall())
c.execute("""DELETE FROM student WHERE rowid % 2 = 0""")


db.commit()
db.close()