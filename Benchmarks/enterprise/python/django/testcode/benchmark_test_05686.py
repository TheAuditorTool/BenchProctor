# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import hashlib
from Crypto.Cipher import AES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05686(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, os.urandom(16))
    ciphertext = cipher.encrypt(str(data).encode().ljust(32)[:32])
    ciphertext = ciphertext + hashlib.md5(ciphertext).hexdigest().encode()
    return JsonResponse({'length': len(ciphertext)}, status=200)
