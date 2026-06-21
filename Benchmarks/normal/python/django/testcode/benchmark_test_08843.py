# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json
import asyncio


def BenchmarkTest08843(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
