# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt
import yaml
import asyncio


def BenchmarkTest10999(request):
    secret_value = 'default_setting_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return JsonResponse({"saved": True})
