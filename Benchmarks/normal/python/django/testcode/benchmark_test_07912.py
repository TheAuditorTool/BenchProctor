# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import asyncio


def BenchmarkTest07912(request):
    secret_value = 'config_secret_test_abc123'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
