# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest53513(request):
    cookie_value = request.COOKIES.get('session_token', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(cookie_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
