# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import json
import asyncio


def BenchmarkTest15428(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
