# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import asyncio
import runpy
from app_runtime import db


def BenchmarkTest08385(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
