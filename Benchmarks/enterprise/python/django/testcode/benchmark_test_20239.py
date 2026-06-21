# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import asyncio
import urllib.parse


def BenchmarkTest20239(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
