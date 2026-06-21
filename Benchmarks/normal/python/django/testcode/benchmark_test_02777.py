# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import asyncio


def BenchmarkTest02777(request):
    raw_body = request.body.decode('utf-8')
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
