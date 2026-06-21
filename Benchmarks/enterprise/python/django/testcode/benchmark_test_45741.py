# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from app_runtime import db


def BenchmarkTest45741(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(db_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
