# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import asyncio


def BenchmarkTest77615(request):
    raw_body = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
