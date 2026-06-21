# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest64989(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = ' '.join(str(header_value).split())
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
