# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import asyncio


def BenchmarkTest15480(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    os.remove(str(data))
    return JsonResponse({"saved": True})
