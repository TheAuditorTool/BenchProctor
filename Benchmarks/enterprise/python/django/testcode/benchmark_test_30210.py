# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import asyncio
from app_runtime import auth_check


def BenchmarkTest30210(request):
    secret_value = 'app_display_name'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
