# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def BenchmarkTest07641(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(auth_header).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
