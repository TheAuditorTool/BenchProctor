# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.decrepit.ciphers.algorithms import ARC4
from cryptography.hazmat.primitives.ciphers import Cipher
import os
import hashlib


def BenchmarkTest00078(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return JsonResponse({'length': len(ciphertext)}, status=200)
