import mysql.connector

mydb = mysql.connector.connect(
  host='db01.codingkids.kadzioch.net',
  user='pyscript',
  password='test#1234%',
  database='pyscript'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM user')

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

