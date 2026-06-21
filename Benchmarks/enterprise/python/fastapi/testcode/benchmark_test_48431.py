# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast
from app_runtime import db


async def BenchmarkTest48431(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
