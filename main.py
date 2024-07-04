import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="SCREENTIME"
)

cursor = db.cursor()

add_record = ("INSERT INTO screen_use_daily (TIME) VALUES (%s)")

txt = """
HOLA AGREGA TU USO DE TELEFONO EL DÍA DE HOY EN HORAS.
EJEMPLO = 3 HORAS Y 30 MINUTOS
ESCRIBIR: 3.5
"""
print(txt)
time = float(input(":"))

x = (time,)
cursor.execute(add_record, x)
db.commit()

cursor.execute("SELECT DAY, TIME FROM screen_use_daily")
for row in cursor:
    date, time = row
    print(f"Date: {date}")
    print(f"Time: {time}")

cursor.close()
db.close()
