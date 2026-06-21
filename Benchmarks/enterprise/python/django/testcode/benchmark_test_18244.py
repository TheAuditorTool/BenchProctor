# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def relay_value(value):
    return value

def BenchmarkTest18244(request):
    raw_body = request.body.decode('utf-8')
    data = relay_value(raw_body)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
