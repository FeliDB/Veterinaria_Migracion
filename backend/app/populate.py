import os
import django
import random
from datetime import datetime, timedelta

# Configuración para ejecutar el script manual fuera de manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from app.models import (
    Dueño, Mascota, Medicamento, TipoFactura, Factura,
    ConsultaVeterinaria, Veterinario, Turno, HistorialClinico
)

def run():
    print("Cargando datos de prueba...")

    # Dueños
    d1 = Dueño.objects.create(dni=123, nombre="Carlos", apellido="Pérez", telefono="+54-911123456")
    d2 = Dueño.objects.create(dni=456, nombre="Laura", apellido="Gómez", telefono="+54-911654321")

    # Mascotas
    m1 = Mascota.objects.create(dueño=d1, nombre="Fido", especie="Perro", raza="Labrador")
    m2 = Mascota.objects.create(dueño=d2, nombre="Mishi", especie="Gato", raza="Persa")

    # Medicamentos
    med1 = Medicamento.objects.create(nombre="Antibiótico X", descripcion="Para infecciones")
    med2 = Medicamento.objects.create(nombre="Vacuna Y", descripcion="Inmunización")

    # Tipo Factura
    tf1 = TipoFactura.objects.create(descripcion="Factura A")
    tf2 = TipoFactura.objects.create(descripcion="Factura B")

    # Facturas
    f1 = Factura.objects.create(
        fecha=datetime.today().date(),
        hora=datetime.now().time(),
        importe=1500.0,
        descripcion="Consulta general",
        tipo_factura=tf1
    )

    f2 = Factura.objects.create(
        fecha=datetime.today().date(),
        hora=datetime.now().time(),
        importe=3000.0,
        descripcion="Consulta + vacuna",
        tipo_factura=tf2
    )

    # Consultas
    c1 = ConsultaVeterinaria.objects.create(
        mascota=m1,
        fecha=datetime.today().date(),
        hora=datetime.now().time(),
        sintoma_principal="Fiebre",
        diagnostico="Infección leve",
        tratamiento="Antibiótico",
        factura=f1
    )

    c2 = ConsultaVeterinaria.objects.create(
        mascota=m2,
        fecha=datetime.today().date(),
        hora=datetime.now().time(),
        sintoma_principal="Alergia",
        diagnostico="Dermatitis",
        tratamiento="Antialérgico",
        factura=f2
    )

    # Veterinarios
    vet1 = Veterinario.objects.create(nombre="Andrés", apellido="Ramírez", especialidad="Dermatología", matricula="VET1234")
    vet2 = Veterinario.objects.create(nombre="María", apellido="Fernández", especialidad="Clínica General", matricula="VET5678")

    # Turnos
    Turno.objects.create(fecha=datetime.today().date(), hora=datetime.now().time(), veterinario=vet1, dueño=d1)
    Turno.objects.create(fecha=datetime.today().date(), hora=datetime.now().time(), veterinario=vet2, dueño=d2)

    # Historiales clínicos
    HistorialClinico.objects.create(mascota=m1, medicamento=med1, consulta=c1)
    HistorialClinico.objects.create(mascota=m2, medicamento=med2, consulta=c2)

    print("✔ Datos cargados correctamente.")

if __name__ == '__main__':
    run()