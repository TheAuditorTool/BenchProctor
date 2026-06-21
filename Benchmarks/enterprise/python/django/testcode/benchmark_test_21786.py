# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import asyncio
import importlib
import sys


def BenchmarkTest21786(request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
