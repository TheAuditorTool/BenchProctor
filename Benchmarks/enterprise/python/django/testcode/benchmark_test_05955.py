# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import asyncio
from app_runtime import db


def BenchmarkTest05955(request):
    multipart_value = request.POST.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
