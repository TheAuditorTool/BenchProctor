# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import db


async def BenchmarkTest30707(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
