# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00039(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
