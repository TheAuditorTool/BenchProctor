# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from Crypto.Cipher import DES


def BenchmarkTest65177(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
