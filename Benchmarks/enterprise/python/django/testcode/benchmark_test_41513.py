# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import asyncio


def BenchmarkTest41513(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    def _primary():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
