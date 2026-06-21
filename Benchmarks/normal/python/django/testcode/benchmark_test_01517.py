# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
import importlib


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01517(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    async def _evasion_task():
        importlib.import_module(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
