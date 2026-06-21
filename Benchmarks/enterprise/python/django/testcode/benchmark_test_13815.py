# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest13815(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
