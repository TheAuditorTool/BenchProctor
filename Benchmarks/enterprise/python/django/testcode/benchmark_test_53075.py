# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest53075(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = handle(referer_value)
    async def _evasion_task():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return asyncio.run(_evasion_task())
