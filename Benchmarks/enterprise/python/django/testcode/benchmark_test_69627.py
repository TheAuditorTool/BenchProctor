# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import asyncio


def BenchmarkTest69627(request):
    multipart_value = request.POST.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(\'<script src="\' + str(data) + \'"></script>\', content_type=\'text/html\')', '<sink>', 'exec'))
    return _ev['r']
