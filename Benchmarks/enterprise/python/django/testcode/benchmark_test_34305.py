# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest34305(request):
    xml_value = request.body.decode('utf-8')
    data = ensure_str(xml_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
