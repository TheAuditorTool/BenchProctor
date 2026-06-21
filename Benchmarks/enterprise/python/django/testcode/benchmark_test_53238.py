# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest53238(request):
    raw_body = request.body.decode('utf-8')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(raw_body).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
