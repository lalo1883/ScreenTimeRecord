# ScreenTimeRecord

## Pasos para Configurar la Base de Datos

### 1. Instalar MySQL
- **Mac**: 
  - Descarga MySQL desde el sitio oficial de MySQL
  - Instala el paquete descargado
  - Añade MySQL a tu PATH si es necesario

- **Windows**:
  - Descarga el instalador de MySQL desde el sitio oficial
  - Ejecuta el instalador y sigue las instrucciones
  - Asegúrate de que MySQL esté en tu PATH

### 2. Crear la Base de Datos y la Tabla
Ejecuta los siguientes comandos en MySQL para crear la base de datos y la tabla:

```sql
CREATE DATABASE SCREENTIME;
USE SCREENTIME;

CREATE TABLE screen_use_daily(
    ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    DAY TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    TIME FLOAT NOT NULL
);

INSERT INTO screen_use_daily (TIME) VALUES (3.5);
SELECT * FROM screen_use_daily;
```

### 3. Crear un entorno virtual
1. Instalar virtualenv:
```bash
pip install virtualenv
```

2. Crear un entorno virtual:
- **Mac/Linux**:
```bash
python3 -m venv myenv
```
- **Windows**:
```bash
python -m venv myenv
```

3. Activar entorno virtual:
- **Mac/Linux**:
```bash
source myenv/bin/activate
```
- **Windows**:
```bash
myenv\Scripts\activate
```

### 4. Instalar mysql-connector-python
```bash
pip install mysql-connector-python
```

### 5. Agregar el siguiente código de Python
Asegúrate de cambiar tus datos en "db":

```python
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
HOLA AGREGA TU USO DE TELÉFONO EL DÍA DE HOY EN HORAS.
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
```



## Crear Alias para Ejecutar Comandos Rápidamente

### macOS (utilizando `.zshrc`)

1. **Abrir el archivo `.zshrc`:**
   - Abre una terminal.
   - Usa el comando `nano ~/.zshrc` para abrir el archivo `.zshrc` en el editor de texto `nano`.

2. **Agregar el alias:**
   - Ve al final del archivo `.zshrc`.
   - Agrega la línea siguiente:
     ```bash
     alias record="cd /ruta/a/tu/archivo && source env/bin/activate && python3 main.py"
     ```
     Reemplaza `/ruta/a/tu/archivo` con la ruta donde se encuentra tu archivo y `main.py` con el nombre de tu script principal si es diferente.

3. **Guardar y salir en `nano`:**
   - Presiona `Ctrl + O` para guardar el archivo.
   - Presiona `Enter` para confirmar el nombre del archivo.
   - Presiona `Ctrl + X` para salir de `nano`.

4. **Recargar `.zshrc`:**
   - Para que los cambios surtan efecto, recarga el archivo `.zshrc` ejecutando `source ~/.zshrc` en la terminal.

5. **Usar el alias:**
   - Después de recargar, puedes usar el comando `record` en la terminal para ejecutar tu script.

### Windows (utilizando PowerShell o CMD)

1. **Abrir el perfil de PowerShell o CMD:**
   - Abre PowerShell o CMD como administrador.

2. **Editar el perfil de PowerShell o CMD:**
   - En PowerShell, puedes editar el perfil ejecutando `notepad $PROFILE`.
   - En CMD, puedes editar el perfil ejecutando `notepad $PROFILE`.

3. **Agregar el alias:**
   - Agrega la línea siguiente al final del archivo:
     ```bash
     function record { Set-Location "C:\ruta\a\tu\archivo"; .\env\Scripts\Activate.ps1; python main.py }
     ```
     Reemplaza `C:\ruta\a\tu\archivo` con la ruta donde se encuentra tu archivo y `main.py` con el nombre de tu script principal si es diferente.

4. **Guardar y cerrar el editor:**
   - Guarda los cambios y cierra el editor.

5. **Recargar el perfil:**
   - En PowerShell, ejecuta `. $PROFILE`.
   - En CMD, cierra y vuelve a abrir la terminal para que los cambios surtan efecto.

6. **Usar el alias:**
   - Después de recargar, puedes usar el comando `record` en PowerShell o CMD para ejecutar tu script.




