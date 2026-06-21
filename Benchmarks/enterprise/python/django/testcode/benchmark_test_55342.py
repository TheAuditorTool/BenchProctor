# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


def BenchmarkTest55342(request):
    host_value = request.META.get('HTTP_HOST', '')
    requested = str(host_value) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(host_value).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
