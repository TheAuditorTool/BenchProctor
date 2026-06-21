# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def BenchmarkTest60323(request):
    raw_body = request.body.decode('utf-8')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(raw_body).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
