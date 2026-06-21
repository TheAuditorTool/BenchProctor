# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest00105(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
