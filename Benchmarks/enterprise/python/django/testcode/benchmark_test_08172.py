# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import asyncio


def BenchmarkTest08172(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(Template(data).render(Context()))", '<sink>', 'exec'))
    return _ev['r']
