# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
import importlib
import sys


def BenchmarkTest31647(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    def _primary():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
