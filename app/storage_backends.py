import os
import base64
from django.core.files.storage import Storage
from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions


class ImageKitMediaStorage(Storage):
    """
    Django Storage backend for ImageKit.io.
    Uploads directly to ImageKit and returns clean CDN URLs.
    """

    def __init__(self):
        self.imagekit = ImageKit(
            private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
            public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
            url_endpoint=os.getenv("IMAGEKIT_URL_ENDPOINT"),
        )

    def _save(self, name, content):
        print(f"🚀 Uploading to ImageKit: {name}")
        try:
            content.seek(0)
            file_data = base64.b64encode(content.read()).decode("utf-8")

            # ✅ Use only filename (no local path)
            clean_name = os.path.basename(name)

            upload_result = self.imagekit.upload_file(
                file=file_data,
                file_name=clean_name,
                options=UploadFileRequestOptions(
                    use_unique_file_name=True,
                    folder="/mahavir_tent_uploads/",
                    is_private_file=False,
                ),
            )

            if upload_result and hasattr(upload_result, "file_path"):
                print(f"✅ Uploaded successfully: {upload_result.url}")
                # ✅ Store only the path part, e.g. mahavir_tent_uploads/abc.jpg
                return upload_result.file_path.strip("/")
            else:
                print("⚠️ Unexpected ImageKit response:", upload_result.__dict__)
                return clean_name
        except Exception as e:
            print(f"❌ Upload failed: {e}")
            return os.path.basename(name)

    def url(self, name):
        """
        Return full CDN URL for the stored file.
        """
        base = os.getenv("IMAGEKIT_URL_ENDPOINT", "").rstrip("/")
        name = name.replace("\\", "/").strip("/")
        # ✅ Ensure correct folder reference
        if not name.startswith("mahavir_tent_uploads/"):
            name = f"mahavir_tent_uploads/{os.path.basename(name)}"
        return f"{base}/{name}"

    def exists(self, name):
        return False
