import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='?',
    password='?',
    database='?'
)

cursor = db.cursor()

# SELECT
# fetchall : todos los registros
# fetchone : el primer registro
def select():
    cursor.execute('select * from Pieza')
    consulta = cursor.fetchall()
    print(consulta)

# INSERT
def insert():
    insertar = 'insert into Pieza(codigo, nombre) values (%s, %s)'
    ejemplar = (404, 'tornillo')
    cursor.execute(insertar, ejemplar)
    db.commit()
    print(cursor.rowcount)

# UPDATE
def update():
    actualizar = 'update Pieza set nombre = %s where codigo = %s'
    ejemplar = ('maquinilla', 404)
    cursor.execute(actualizar, ejemplar)
    db.commit()

# DELETE
def delete():
    eliminar = 'delete from Pieza where codigo = %s'
    ejemplar = (404, )
    cursor.execute(eliminar, ejemplar)
    db.commit()
