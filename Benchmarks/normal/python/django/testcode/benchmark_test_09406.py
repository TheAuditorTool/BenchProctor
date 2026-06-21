# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import asyncio


def BenchmarkTest09406(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    async def _evasion_task():
        yaml.load(data, Loader=yaml.UnsafeLoader)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
