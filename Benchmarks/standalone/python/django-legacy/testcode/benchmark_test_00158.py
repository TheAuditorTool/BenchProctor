# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import os
import hashlib
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00158(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = algorithms.ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return JsonResponse({'length': len(ciphertext)}, status=200)
