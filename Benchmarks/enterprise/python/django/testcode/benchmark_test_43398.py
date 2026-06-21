# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def BenchmarkTest43398(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(cookie_value).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
