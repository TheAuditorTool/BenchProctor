# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json
import asyncio


def BenchmarkTest28506(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    async def _evasion_task():
        subprocess.run('echo ' + str(data), shell=True)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
