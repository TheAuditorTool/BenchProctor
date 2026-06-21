# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os
import asyncio


def BenchmarkTest48601(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
