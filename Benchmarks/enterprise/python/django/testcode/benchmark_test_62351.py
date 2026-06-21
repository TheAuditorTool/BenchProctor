# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62351(request):
    host_value = request.META.get('HTTP_HOST', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
