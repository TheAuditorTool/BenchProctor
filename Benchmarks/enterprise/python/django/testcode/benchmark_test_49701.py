# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json
import asyncio


def BenchmarkTest49701(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
