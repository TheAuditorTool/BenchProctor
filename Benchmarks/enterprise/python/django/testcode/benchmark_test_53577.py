# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import asyncio


def BenchmarkTest53577(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
