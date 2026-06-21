# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import asyncio


def BenchmarkTest04458(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
