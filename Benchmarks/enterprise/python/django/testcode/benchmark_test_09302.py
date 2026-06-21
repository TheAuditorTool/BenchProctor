# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
import asyncio


def BenchmarkTest09302(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
