# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import hashlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


def BenchmarkTest00536(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    _des_key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()[:8]
    ciphertext = DES.new(_des_key, DES.MODE_ECB).encrypt(pad(str(data).encode(), 8))
    return JsonResponse({'length': len(ciphertext)}, status=200)
