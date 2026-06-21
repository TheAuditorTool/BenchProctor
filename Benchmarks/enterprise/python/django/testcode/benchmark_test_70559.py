# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio


def BenchmarkTest70559(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
