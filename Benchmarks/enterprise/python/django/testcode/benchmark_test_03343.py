# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest03343(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode())
    with open('/var/data/secrets.enc', 'wb') as fh:
        fh.write(encrypted)
    return JsonResponse({"saved": True})
