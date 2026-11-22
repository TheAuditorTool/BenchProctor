import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import uvicorn
from django.core.asgi import get_asgi_application

application = get_asgi_application()


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8000)
