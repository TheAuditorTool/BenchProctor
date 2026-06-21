# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest01626(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
