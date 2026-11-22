# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import os
import hashlib


def BenchmarkTest00193(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = algorithms.ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return JsonResponse({'length': len(ciphertext)}, status=200)
