# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import asyncio


def BenchmarkTest57146(request):
    upload_name = request.FILES['upload'].name
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(Template(data).render(Context()))", '<sink>', 'exec'))
    return _ev['r']
