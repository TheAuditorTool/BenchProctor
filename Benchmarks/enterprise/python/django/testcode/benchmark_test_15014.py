# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


@dataclass
class FormData:
    payload: str

def BenchmarkTest15014(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
