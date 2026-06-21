# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import db


async def BenchmarkTest49192(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
