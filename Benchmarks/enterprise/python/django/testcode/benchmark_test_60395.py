# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import re
import asyncio


def BenchmarkTest60395(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
