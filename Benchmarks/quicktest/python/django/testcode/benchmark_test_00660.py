# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
import asyncio


def BenchmarkTest00660(request):
    host_value = request.META.get('HTTP_HOST', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
