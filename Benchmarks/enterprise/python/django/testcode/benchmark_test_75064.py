# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import asyncio
from app_runtime import db


def BenchmarkTest75064(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(Template(data).render(Context()))", '<sink>', 'exec'))
    return _ev['r']
