# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def BenchmarkTest01110(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(json_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
