# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02302(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
