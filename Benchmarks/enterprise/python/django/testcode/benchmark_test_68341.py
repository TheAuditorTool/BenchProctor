# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from app_runtime import db


def BenchmarkTest68341(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(comment_value).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
