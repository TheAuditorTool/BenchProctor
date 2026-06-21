# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest69147(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    key = os.environ['DATA_ENC_KEY'].encode()
    globals().setdefault('_secret_cache', {})['current'] = Fernet(key).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
