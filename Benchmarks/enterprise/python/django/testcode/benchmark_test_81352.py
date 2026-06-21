# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES
from Crypto.Cipher import AES


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest81352(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = handle(cookie_value)
    requested = str(data) or 'DES'
    if requested == 'AES':
        cipher = AES.new(b'0123456789abcdef', AES.MODE_ECB)
    else:
        cipher = DES.new(b'legacyky', DES.MODE_ECB)
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return JsonResponse({'length': len(ciphertext)}, status=200)
