# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
import asyncio


def BenchmarkTest08364(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
