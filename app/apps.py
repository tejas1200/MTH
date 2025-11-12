from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

from django.apps import AppConfig


class AppConfigWithStorage(AppConfig):
    name = "app"
    verbose_name = "Mahavir Tent House"

    def ready(self):
        # ✅ Safe import (after Django settings loaded)
        from django.conf import settings
        from django.core.files.storage import storages

        if (
            hasattr(settings, "DEFAULT_FILE_STORAGE")
            and settings.DEFAULT_FILE_STORAGE == "app.storage_backends.ImageKitMediaStorage"
        ):
            try:
                from app.storage_backends import ImageKitMediaStorage

                storages._storages["default"] = ImageKitMediaStorage()
                print("✅ ImageKitMediaStorage initialized successfully")
            except Exception as e:
                print("⚠️ Failed to initialize ImageKitMediaStorage:", e)
