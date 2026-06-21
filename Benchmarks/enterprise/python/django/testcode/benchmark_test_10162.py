# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest10162(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(json_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
