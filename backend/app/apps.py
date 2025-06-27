from django.apps import AppConfig
from django.db.utils import OperationalError


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        # Para evitar errores en migrate
        import os
        import app.signals
        if os.environ.get("RUN_MAIN") != "true":
            return

        from django.db import connection
        from django.core.exceptions import ObjectDoesNotExist
        from app.models import Dueño

        try:
            # Verificamos si ya hay datos
            if Dueño.objects.exists():
                return  # Ya hay datos, no hacemos nada

            print("🧪 Cargando datos de prueba en la base de datos PostgreSQL...")
            from .populate import run
            run()
            print("✔ Carga inicial completada.")

        except OperationalError:
            print("⛔ Aún no hay tablas. La carga inicial se omitió.")