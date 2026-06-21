# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest33076(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(auth_header).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
