# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import asyncio


def BenchmarkTest20760(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(\'<script src="\' + str(data) + \'"></script>\', content_type=\'text/html\')', '<sink>', 'exec'))
    return _ev['r']
