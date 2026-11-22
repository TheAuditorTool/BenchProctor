# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import json
import os
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00244(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(str(data).encode()) + padder.finalize()
    encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return JsonResponse({'length': len(ciphertext)}, status=200)
