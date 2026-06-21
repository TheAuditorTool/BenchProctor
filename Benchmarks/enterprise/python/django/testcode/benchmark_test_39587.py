# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Cipher import DES


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest39587(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return JsonResponse({'length': len(ciphertext)}, status=200)
