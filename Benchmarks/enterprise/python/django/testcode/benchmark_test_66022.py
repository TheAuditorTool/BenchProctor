# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from Crypto.Cipher import DES
from Crypto.Cipher import AES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest66022(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    requested = str(data) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
