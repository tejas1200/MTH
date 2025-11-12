# Force Django to use ImageKit as the default storage backend

from django.conf import settings
from django.core.files.storage import storages

# Only override if the setting points to your class
if settings.DEFAULT_FILE_STORAGE == "app.storage_backends.ImageKitMediaStorage":
    from app.storage_backends import ImageKitMediaStorage
    storages._storages["default"] = ImageKitMediaStorage()
