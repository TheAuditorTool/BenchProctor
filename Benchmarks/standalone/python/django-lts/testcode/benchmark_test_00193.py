# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
import hashlib


def BenchmarkTest00193(request):
    user_id = request.GET.get('id', '')
    kind = 'json' if str(user_id).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(user_id).strip()
        case _:
            data = str(user_id)
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + ChaCha20Poly1305(key).encrypt(nonce, str(data).encode(), None)
    return JsonResponse({'length': len(ciphertext)}, status=200)
