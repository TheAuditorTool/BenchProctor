# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest58949(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
