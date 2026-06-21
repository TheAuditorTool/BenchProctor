# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import os
import asyncio
from app_runtime import db


def BenchmarkTest12477(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
