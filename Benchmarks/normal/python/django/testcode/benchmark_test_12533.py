# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
from app_runtime import auth_check


def BenchmarkTest12533(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = asyncio.run(fetch_payload())
    auth_check('user', data)
    return JsonResponse({"saved": True})
