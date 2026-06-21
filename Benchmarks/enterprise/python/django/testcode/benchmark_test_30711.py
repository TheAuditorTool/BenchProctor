# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest30711(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(auth_header).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
