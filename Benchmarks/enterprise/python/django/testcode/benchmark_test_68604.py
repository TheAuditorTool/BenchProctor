# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from Crypto.Cipher import DES


def BenchmarkTest68604(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
