# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import runpy


def relay_value(value):
    return value

def BenchmarkTest76486(request, path_param):
    path_value = path_param
    data = relay_value(path_value)
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
