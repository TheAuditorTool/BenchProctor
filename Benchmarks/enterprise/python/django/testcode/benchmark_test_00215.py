# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from Crypto.Cipher import AES


def BenchmarkTest00215(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
