# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import asyncio


def BenchmarkTest29570(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
