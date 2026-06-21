# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from Crypto.Cipher import DES


def BenchmarkTest64518(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
