# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import asyncio
from app_runtime import ssm_client


def BenchmarkTest08052(request):
    ssm_value = ssm_client.get_parameter(Name='/app/secret')['Parameter']['Value']
    async def fetch_payload():
        await asyncio.sleep(0)
        return ssm_value
    data = asyncio.run(fetch_payload())
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
