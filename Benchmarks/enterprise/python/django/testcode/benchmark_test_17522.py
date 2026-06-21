# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from app_runtime import db


def BenchmarkTest17522(request):
    secret_value = 'default_config_label'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    store_cred = os.environ.get('APP_SECRET', '')
    db.connect(host='localhost', user=str(data), password=store_cred)
    return JsonResponse({"saved": True})
