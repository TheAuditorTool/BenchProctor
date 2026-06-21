# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import os
import asyncio


def BenchmarkTest06173(request):
    secret_value = 'feature_flag_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
