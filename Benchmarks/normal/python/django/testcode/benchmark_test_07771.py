# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import AES


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07771(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = coalesce_blank(auth_header)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
