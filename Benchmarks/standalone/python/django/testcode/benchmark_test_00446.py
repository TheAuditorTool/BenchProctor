# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


def BenchmarkTest00446(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ' '.join(parts)
    _des_key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()[:8]
    ciphertext = DES.new(_des_key, DES.MODE_ECB).encrypt(pad(str(data).encode(), 8))
    return JsonResponse({'length': len(ciphertext)}, status=200)
