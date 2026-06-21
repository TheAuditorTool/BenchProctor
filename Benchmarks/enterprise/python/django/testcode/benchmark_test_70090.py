# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import pickle


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest70090(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = handle(ua_value)
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
