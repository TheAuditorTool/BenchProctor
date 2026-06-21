# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import ast
from app_runtime import db


async def BenchmarkTest21351(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        return HTMLResponse('<div>' + str(data) + '</div>')
    return await _evasion_task()
