# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio


def BenchmarkTest17903(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    int(str(data))
    return JsonResponse({"saved": True})
