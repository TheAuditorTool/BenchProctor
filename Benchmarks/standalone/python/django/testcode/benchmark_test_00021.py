# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from dataclasses import dataclass
import os
import hashlib
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00021(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    form = FormData(payload=db_value)
    data = form.payload
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + ChaCha20Poly1305(key).encrypt(nonce, str(data).encode(), None)
    return JsonResponse({'length': len(ciphertext)}, status=200)
