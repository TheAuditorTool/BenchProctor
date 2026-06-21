# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import ast
import asyncio


def BenchmarkTest73569(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
