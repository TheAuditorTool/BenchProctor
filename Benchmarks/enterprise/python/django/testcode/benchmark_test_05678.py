# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest05678(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
