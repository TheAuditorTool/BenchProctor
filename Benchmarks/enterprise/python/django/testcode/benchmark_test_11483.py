# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from Crypto.Cipher import DES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest11483(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
