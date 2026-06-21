# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os
import asyncio


def relay_value(value):
    return value

def BenchmarkTest43894(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    async def _evasion_task():
        subprocess.Popen('echo ' + str(data), shell=True).wait()
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
