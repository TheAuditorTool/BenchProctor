# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import asyncio


def BenchmarkTest06002(request):
    host_value = request.META.get('HTTP_HOST', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    async def _evasion_task():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return asyncio.run(_evasion_task())
