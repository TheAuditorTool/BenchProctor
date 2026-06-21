# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


def BenchmarkTest05551(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    requested = str(origin_value) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(origin_value).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
