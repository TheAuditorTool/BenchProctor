# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import time
import asyncio
from app_runtime import db


def BenchmarkTest17330(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
