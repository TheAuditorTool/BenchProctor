# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest51548(request):
    xml_value = request.body.decode('utf-8')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(xml_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
