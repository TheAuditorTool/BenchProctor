# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import asyncio


def BenchmarkTest60161(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
