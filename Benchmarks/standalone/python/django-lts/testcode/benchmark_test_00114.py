# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.decrepit.ciphers.algorithms import ARC4
from cryptography.hazmat.primitives.ciphers import Cipher
import os
import hashlib
from app_runtime import db


def BenchmarkTest00114(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return JsonResponse({'length': len(ciphertext)}, status=200)
