# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from Crypto.Cipher import DES


def to_text(value):
    return str(value).strip()

def BenchmarkTest48854(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
