# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio
import ctypes


def BenchmarkTest62610(request, path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
