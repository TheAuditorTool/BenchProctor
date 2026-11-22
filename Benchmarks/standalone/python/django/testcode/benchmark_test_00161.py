# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import json
import os
import hashlib


def BenchmarkTest00161(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + ChaCha20Poly1305(key).encrypt(nonce, str(data).encode(), None)
    return JsonResponse({'length': len(ciphertext)}, status=200)
