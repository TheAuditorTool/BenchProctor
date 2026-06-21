# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import asyncio


def BenchmarkTest06757(request):
    xml_value = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
