# # core/__init__.py
# """
# Safe ImageKit integration initializer.
# Avoids touching Django settings before configuration is complete.
# """

# import os

# # Only run this block after Django is initialized
# def setup_imagekit_storage():
#     try:
#         from django.conf import settings
#         from django.core.files.storage import storages
#         from app.storage_backends import ImageKitMediaStorage

#         if getattr(settings, "DEFAULT_FILE_STORAGE", None) == "app.storage_backends.ImageKitMediaStorage":
#             storages._storages["default"] = ImageKitMediaStorage()
#     except Exception as e:
#         # Avoid breaking startup if settings aren't ready yet
#         print(f"⚠️ ImageKit setup skipped: {e}")

# # Optionally call later from apps.py or after startup
# if os.getenv("RUN_MAIN") == "true":  # only run once, not in autoreload
#     setup_imagekit_storage()
