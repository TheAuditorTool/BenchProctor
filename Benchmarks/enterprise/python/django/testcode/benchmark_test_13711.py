# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest13711(request, path_param):
    path_value = path_param
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(path_value).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
