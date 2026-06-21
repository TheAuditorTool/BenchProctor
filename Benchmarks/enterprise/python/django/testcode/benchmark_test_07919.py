# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07919(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
