# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import asyncio


def BenchmarkTest58095(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return asyncio.run(_evasion_task())
