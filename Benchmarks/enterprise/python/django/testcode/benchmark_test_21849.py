# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import asyncio
import urllib.parse


def BenchmarkTest21849(request):
    user_id = request.GET.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
