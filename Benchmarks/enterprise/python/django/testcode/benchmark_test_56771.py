# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def BenchmarkTest56771(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(ua_value).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
