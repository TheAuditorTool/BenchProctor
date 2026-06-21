# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
from Crypto.Cipher import AES


@dataclass
class FormData:
    payload: str

def BenchmarkTest12368(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
