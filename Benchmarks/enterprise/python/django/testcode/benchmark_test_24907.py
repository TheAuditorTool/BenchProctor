# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest24907(request):
    env_value = os.environ.get('USER_INPUT', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(env_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
