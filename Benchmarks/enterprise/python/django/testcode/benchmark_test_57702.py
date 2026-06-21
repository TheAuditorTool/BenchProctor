# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
import asyncio


def BenchmarkTest57702(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = asyncio.run(fetch_payload())
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
