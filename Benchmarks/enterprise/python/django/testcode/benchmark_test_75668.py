# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest75668(request):
    raw_body = request.body.decode('utf-8')
    data = handle(raw_body)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
