Acceder a bases de datos con python

MYSQL

crear usuario:
  -> create user '<user>'@'localhost'
  -> identified with mysql_native_password by '<password>';

otorgar permisos a usuario:
  -> grant all privileges on *.* to '<user>'@'localhost';

conectar con la base de datos
db = mysql.connector.connect(
  host, user, password, database
  )

objeto para ejecutar consultas
cursor = db.cursor()
