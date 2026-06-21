# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


@dataclass
class FormData:
    payload: str

def BenchmarkTest11948(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
