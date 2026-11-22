# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import hashlib


def BenchmarkTest00191(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip!s}'
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(str(data).encode()) + padder.finalize()
    encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return JsonResponse({'length': len(ciphertext)}, status=200)
