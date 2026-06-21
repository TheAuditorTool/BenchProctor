# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from Crypto.Cipher import DES


def BenchmarkTest20736(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
