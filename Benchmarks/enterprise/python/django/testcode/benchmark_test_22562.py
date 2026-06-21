# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from Crypto.Cipher import DES


def BenchmarkTest22562(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(json_value).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
