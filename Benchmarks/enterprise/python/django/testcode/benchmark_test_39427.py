# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
import asyncio


def BenchmarkTest39427(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(mark_safe('<div>' + str(data) + '</div>'))", '<sink>', 'exec'))
    return _ev['r']
