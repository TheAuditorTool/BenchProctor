# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest30460(request):
    env_value = os.environ.get('USER_INPUT', '')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(env_value).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
