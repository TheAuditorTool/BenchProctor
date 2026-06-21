# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import json
import asyncio


def BenchmarkTest33114(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return asyncio.run(_evasion_task())
