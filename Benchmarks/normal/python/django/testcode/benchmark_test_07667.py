# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest07667(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
