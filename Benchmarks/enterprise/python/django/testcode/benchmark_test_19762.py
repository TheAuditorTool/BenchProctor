# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import asyncio


def BenchmarkTest19762(request):
    cookie_value = request.COOKIES.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
