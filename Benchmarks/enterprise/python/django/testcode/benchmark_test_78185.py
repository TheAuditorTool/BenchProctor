# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import asyncio
from types import SimpleNamespace


def BenchmarkTest78185(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return redirect(str(data))
    return asyncio.run(_evasion_task())
