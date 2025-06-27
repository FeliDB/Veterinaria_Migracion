import psycopg2
from pymongo import MongoClient

# Conexión a PostgreSQL
pg_conn = psycopg2.connect(
    host="localhost",
    database="veterinaria",
    user="usuario",
    password="12345",
    port=5432
)
pg_cursor = pg_conn.cursor()

# Conexión a MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["veterinaria_mongo"]

def migrate_dueño():
    pg_cursor.execute("SELECT dni, nombre, apellido, telefono FROM app_dueño")
    for dni, nombre, apellido, telefono in pg_cursor.fetchall():
        mongo_db.dueño.update_one(
            {"dni": dni},
            {"$set": {
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono
            }},
            upsert=True
        )

def migrate_mascota():
    pg_cursor.execute("SELECT id, dueño_id, nombre, especie, raza FROM app_mascota")
    for id_, dueño_id, nombre, especie, raza in pg_cursor.fetchall():
        mongo_db.mascota.update_one(
            {"_id": id_},
            {"$set": {
                "dueño": dueño_id,
                "nombre": nombre,
                "especie": especie,
                "raza": raza
            }},
            upsert=True
        )

def migrate_medicamento():
    pg_cursor.execute("SELECT id, nombre, descripcion FROM app_medicamento")
    for id_, nombre, descripcion in pg_cursor.fetchall():
        mongo_db.medicamento.update_one(
            {"_id": id_},
            {"$set": {
                "nombre": nombre,
                "descripcion": descripcion
            }},
            upsert=True
        )

def migrate_tipo_factura():
    pg_cursor.execute("SELECT id, descripcion FROM app_tipofactura")
    for id_, descripcion in pg_cursor.fetchall():
        mongo_db.tipo_factura.update_one(
            {"_id": id_},
            {"$set": {
                "descripcion": descripcion
            }},
            upsert=True
        )

def migrate_factura():
    pg_cursor.execute("SELECT id, fecha, hora, importe, descripcion, tipo_factura_id FROM app_factura")
    for id_, fecha, hora, importe, descripcion, tipo_factura_id in pg_cursor.fetchall():
        mongo_db.factura.update_one(
            {"_id": id_},
            {"$set": {
                "fecha": fecha.isoformat(),
                "hora": str(hora),
                "importe": importe,
                "descripcion": descripcion,
                "tipo_factura": tipo_factura_id
            }},
            upsert=True
        )

def migrate_consulta_veterinaria():
    pg_cursor.execute("""SELECT id, mascota_id, fecha, hora, sintoma_principal, diagnostico, tratamiento, factura_id
                         FROM app_consultaveterinaria""")
    for id_, mascota_id, fecha, hora, sintoma_principal, diagnostico, tratamiento, factura_id in pg_cursor.fetchall():
        mongo_db.consulta_veterinaria.update_one(
            {"_id": id_},
            {"$set": {
                "mascota": mascota_id,
                "fecha": fecha.isoformat(),
                "hora": str(hora),
                "sintoma_principal": sintoma_principal,
                "diagnostico": diagnostico,
                "tratamiento": tratamiento,
                "factura": factura_id
            }},
            upsert=True
        )

def migrate_veterinario():
    pg_cursor.execute("SELECT id, nombre, apellido, especialidad, matricula FROM app_veterinario")
    for id_, nombre, apellido, especialidad, matricula in pg_cursor.fetchall():
        mongo_db.veterinario.update_one(
            {"_id": id_},
            {"$set": {
                "nombre": nombre,
                "apellido": apellido,
                "especialidad": especialidad,
                "matricula": matricula
            }},
            upsert=True
        )

def migrate_turno():
    pg_cursor.execute("SELECT id, fecha, hora, veterinario_id, dueño_id FROM app_turno")
    for id_, fecha, hora, veterinario_id, dueño_id in pg_cursor.fetchall():
        mongo_db.turno.update_one(
            {"_id": id_},
            {"$set": {
                "fecha": fecha.isoformat(),
                "hora": str(hora),
                "veterinario": veterinario_id,
                "dueño": dueño_id
            }},
            upsert=True
        )

def migrate_historial_clinico():
    pg_cursor.execute("SELECT id, mascota_id, medicamento_id, consulta_id FROM app_historialclinico")
    for id_, mascota_id, medicamento_id, consulta_id in pg_cursor.fetchall():
        mongo_db.historial_clinico.update_one(
            {"_id": id_},
            {"$set": {
                "mascota": mascota_id,
                "medicamento": medicamento_id,
                "consulta": consulta_id
            }},
            upsert=True
        )

if __name__ == "__main__":
    migrate_dueño()
    migrate_mascota()
    migrate_medicamento()
    migrate_tipo_factura()
    migrate_factura()
    migrate_consulta_veterinaria()
    migrate_veterinario()
    migrate_turno()
    migrate_historial_clinico()
    print("Migración a MongoDB completada.")
