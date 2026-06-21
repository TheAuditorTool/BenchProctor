# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import asyncio
from types import SimpleNamespace


def BenchmarkTest62628(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return HttpResponse(mark_safe('<img src="' + str(data) + '">'))
    return asyncio.run(_evasion_task())
