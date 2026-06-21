# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import db


async def BenchmarkTest29558(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    async def _evasion_task():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    await _evasion_task()
    return {"updated": True}
