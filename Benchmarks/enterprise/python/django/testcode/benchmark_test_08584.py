# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest08584(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    try:
        _bounded = int(data)
        if _bounded < 0 or _bounded > 10000:
            return JsonResponse({'error': 'out of range'}, status=400)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
