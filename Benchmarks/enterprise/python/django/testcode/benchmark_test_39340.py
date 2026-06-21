# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
import asyncio


def BenchmarkTest39340(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
