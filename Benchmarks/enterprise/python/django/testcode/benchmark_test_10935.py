# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import hashlib
from Crypto.Cipher import AES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest10935(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return JsonResponse({'length': len(ciphertext)}, status=200)
