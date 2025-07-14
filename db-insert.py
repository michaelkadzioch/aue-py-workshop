import mysql.connector

mydb = mysql.connector.connect(
  host='db01.codingkids.kadzioch.net',
  user='pyscript',
  password='test#1234%',
  database='pyscript'
)

mycursor = mydb.cursor()

# Einfügen einer neuen Zeile in die Tabelle user
sql = "INSERT INTO user (username, passhash) VALUES (%s, %s)"
val = ('Huge123', 'test#1234567890')
mycursor.execute(sql, val)

mydb.commit()


# Abfrage id und username aus der Tabelle user
mycursor.execute('SELECT id, username, passhash FROM user')

myresult = mycursor.fetchall()

for x in myresult:
  print(x)