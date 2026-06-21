# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
import importlib
import sys


def coalesce_blank(value):
    return value or ''

def BenchmarkTest78775(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
