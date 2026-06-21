# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import asyncio
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest01922(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return asyncio.run(_evasion_task())
