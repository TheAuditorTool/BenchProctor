# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os
import asyncio


def BenchmarkTest64247(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        return HttpResponse(Template(data).render(Context()))
    return JsonResponse({"saved": True})
