# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from app_runtime import db


def BenchmarkTest02233(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    try:
        int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return JsonResponse({'length': len(ciphertext)}, status=200)
