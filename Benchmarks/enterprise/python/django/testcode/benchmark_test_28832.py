# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import os
import asyncio


def BenchmarkTest28832(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return JsonResponse({"saved": True})
