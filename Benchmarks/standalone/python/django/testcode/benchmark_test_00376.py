# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


def BenchmarkTest00376(request):
    user_id = request.GET.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    _des_key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()[:8]
    ciphertext = DES.new(_des_key, DES.MODE_ECB).encrypt(pad(str(data).encode(), 8))
    return JsonResponse({'length': len(ciphertext)}, status=200)
