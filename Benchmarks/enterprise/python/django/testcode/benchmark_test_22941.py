# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest22941(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(processed).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
