# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json
import os


def BenchmarkTest00594(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = f'{json_value!s}'
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
