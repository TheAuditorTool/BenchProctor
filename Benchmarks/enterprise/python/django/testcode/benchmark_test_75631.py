# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest75631(request):
    xml_value = request.body.decode('utf-8')
    data = coalesce_blank(xml_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
