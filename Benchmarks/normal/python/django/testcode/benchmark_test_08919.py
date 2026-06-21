# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from Crypto.Cipher import AES
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest08919(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
