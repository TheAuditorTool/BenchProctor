# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
import asyncio


def BenchmarkTest36628(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
