# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import asyncio
from app_runtime import db


def BenchmarkTest65026(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    def _primary():
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
