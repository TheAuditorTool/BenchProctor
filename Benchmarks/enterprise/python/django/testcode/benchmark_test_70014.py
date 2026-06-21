# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest70014(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = handle(host_value)
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
