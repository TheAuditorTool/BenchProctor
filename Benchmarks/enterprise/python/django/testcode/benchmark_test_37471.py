# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest37471(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
