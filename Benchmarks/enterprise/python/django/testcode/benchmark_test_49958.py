# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import boto3
import asyncio
from app_runtime import db


def BenchmarkTest49958(request):
    secret_value = 'default_config_label'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    sm = boto3.client('secretsmanager')
    store_cred = sm.get_secret_value(SecretId='app/secret')['SecretString']
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
