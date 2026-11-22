# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00109(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    reader = make_reader(ua_value)
    data = reader()
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + AESGCM(key).encrypt(nonce, str(data).encode(), None)
    return JsonResponse({'length': len(ciphertext)}, status=200)
