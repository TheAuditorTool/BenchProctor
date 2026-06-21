# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import asyncio


def ensure_str(value):
    return str(value)

def BenchmarkTest07995(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ensure_str(auth_header)
    async def _evasion_task():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return asyncio.run(_evasion_task())
