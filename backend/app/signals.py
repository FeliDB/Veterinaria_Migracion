from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from app.models import Dueño
from django.db.utils import OperationalError


@receiver(post_migrate)
def populate_data(sender, **kwargs):
    if sender.name != "app":
        return

    try:
        if Dueño.objects.exists():
            return  # Ya hay datos

        from app.populate import run
        print("⚙️ Insertando datos de prueba...")
        run()
        print("✅ Datos insertados correctamente.")
    except OperationalError as e:
        print(f"⚠️ Error de base de datos: {e}")