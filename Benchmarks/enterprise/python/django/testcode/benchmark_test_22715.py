# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import re
import asyncio


def BenchmarkTest22715(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return JsonResponse({"saved": True})
