# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
from Crypto.Cipher import AES


def BenchmarkTest34417(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
