# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import asyncio


def BenchmarkTest26923(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
