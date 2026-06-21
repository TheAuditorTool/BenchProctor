# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06811(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
