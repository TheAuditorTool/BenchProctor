# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
import asyncio


def BenchmarkTest65032(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
