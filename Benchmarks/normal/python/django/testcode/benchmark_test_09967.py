# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os
import hashlib
from Crypto.Cipher import AES


@dataclass
class FormData:
    payload: str

def BenchmarkTest09967(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = FormData(payload=auth_header).payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return JsonResponse({'length': len(ciphertext)}, status=200)
