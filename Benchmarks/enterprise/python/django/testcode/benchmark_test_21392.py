# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
import importlib
import sys


request_state: dict[str, str] = {}

def BenchmarkTest21392(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
