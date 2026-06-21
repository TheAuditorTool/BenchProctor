# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


def BenchmarkTest57830(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    requested = str(header_value) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(header_value).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
