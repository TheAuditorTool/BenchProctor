# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import asyncio


def BenchmarkTest70032(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
