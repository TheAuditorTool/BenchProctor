# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
import asyncio
import subprocess
from app_runtime import db


def BenchmarkTest10637(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return JsonResponse({"saved": True})
