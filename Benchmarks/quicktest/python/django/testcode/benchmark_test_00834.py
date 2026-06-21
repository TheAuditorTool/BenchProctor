# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest00834(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
