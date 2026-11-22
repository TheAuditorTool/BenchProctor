# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import json
import os
import hashlib


def BenchmarkTest00030(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + AESGCM(key).encrypt(nonce, str(data).encode(), None)
    return JsonResponse({'length': len(ciphertext)}, status=200)
