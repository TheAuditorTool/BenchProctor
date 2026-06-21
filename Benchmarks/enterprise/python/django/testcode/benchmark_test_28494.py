# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import AES


def BenchmarkTest28494(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(ua_value).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
