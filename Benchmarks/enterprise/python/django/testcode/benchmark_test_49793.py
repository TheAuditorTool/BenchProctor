# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
import asyncio


def BenchmarkTest49793(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return config_value
    data = asyncio.run(fetch_payload())
    key = os.environ['DATA_ENC_KEY'].encode()
    encrypted = Fernet(key).encrypt(str(data).encode()).decode()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', encrypted, secure=True, httponly=True, samesite='Strict')
    return resp
