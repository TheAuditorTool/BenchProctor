# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json
import asyncio


def BenchmarkTest56548(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
