# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from Crypto.Cipher import AES


def BenchmarkTest28762(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(json_value).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
