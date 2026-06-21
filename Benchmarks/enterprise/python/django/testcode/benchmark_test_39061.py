# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import asyncio


def BenchmarkTest39061(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
