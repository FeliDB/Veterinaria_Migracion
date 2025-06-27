from django.db import models


class Dueño(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)  # para poder poner +54, guiones, etc.

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Mascota(models.Model):
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoFactura(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Factura(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    importe = models.FloatField()
    descripcion = models.CharField(max_length=100)
    tipo_factura = models.ForeignKey(TipoFactura, on_delete=models.CASCADE, related_name='facturas')

    def __str__(self):
        return f"Factura {self.id} - {self.descripcion}"


class ConsultaVeterinaria(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='consultas')
    fecha = models.DateField()
    hora = models.TimeField()
    sintoma_principal = models.TextField()
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='consultas')

    def __str__(self):
        return f"Consulta {self.id} - {self.fecha}"


class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='turnos')
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE, related_name='turnos')

    def __str__(self):
        return f"Turno {self.id} - {self.fecha} {self.hora}"


class HistorialClinico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='historial_clinico')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='historiales')
    consulta = models.ForeignKey(ConsultaVeterinaria, on_delete=models.CASCADE, related_name='historiales')

    def __str__(self):
        return f"Historial {self.id} - Mascota {self.mascota.nombre}"