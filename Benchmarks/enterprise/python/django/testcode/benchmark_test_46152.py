# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import asyncio


def BenchmarkTest46152(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return query_array
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
