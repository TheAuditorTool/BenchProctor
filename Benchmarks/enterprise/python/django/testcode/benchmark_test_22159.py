# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import ast
import asyncio
from app_runtime import db


def BenchmarkTest22159(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return asyncio.run(_evasion_task())
