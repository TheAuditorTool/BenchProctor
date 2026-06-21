# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import sys
import asyncio


def BenchmarkTest06525(request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return argv_value
    data = asyncio.run(fetch_payload())
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return JsonResponse({"saved": True})
