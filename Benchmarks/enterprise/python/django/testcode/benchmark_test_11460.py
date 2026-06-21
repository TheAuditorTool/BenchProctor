# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest11460(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(ua_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
