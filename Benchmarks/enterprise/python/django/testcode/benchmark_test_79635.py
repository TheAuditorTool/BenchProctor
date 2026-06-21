# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
import hashlib
from Crypto.Cipher import AES


def BenchmarkTest79635(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return JsonResponse({'length': len(ciphertext)}, status=200)
