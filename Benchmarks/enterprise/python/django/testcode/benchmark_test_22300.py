# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import ctypes
from app_runtime import db


def BenchmarkTest22300(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
