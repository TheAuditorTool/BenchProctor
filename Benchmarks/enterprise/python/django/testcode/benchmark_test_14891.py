# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
import ast
import asyncio
from app_runtime import db


def BenchmarkTest14891(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    async def _evasion_task():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
