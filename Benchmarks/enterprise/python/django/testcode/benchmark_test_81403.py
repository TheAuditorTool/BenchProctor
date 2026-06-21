# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def BenchmarkTest81403(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    key = RSA.generate(2048)
    ciphertext = PKCS1_v1_5.new(key).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
