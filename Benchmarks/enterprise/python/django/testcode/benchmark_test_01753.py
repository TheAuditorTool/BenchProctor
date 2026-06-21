# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest01753(request):
    multipart_value = request.POST.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
