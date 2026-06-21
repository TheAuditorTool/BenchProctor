# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import asyncio


def BenchmarkTest53325(request):
    raw_body = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.chmod('/var/app/data/' + str(processed), 0o777)
    return JsonResponse({"saved": True})
