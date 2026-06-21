# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import asyncio


def BenchmarkTest58042(request):
    multipart_value = request.POST.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
