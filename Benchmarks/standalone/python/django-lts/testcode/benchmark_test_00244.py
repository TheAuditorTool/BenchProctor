# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os
import hashlib


def BenchmarkTest00244(request):
    field_value = request.POST.get('field', '')
    data = ' '.join(str(field_value).split())
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + ChaCha20Poly1305(key).encrypt(nonce, str(data).encode(), None)
    return JsonResponse({'length': len(ciphertext)}, status=200)
