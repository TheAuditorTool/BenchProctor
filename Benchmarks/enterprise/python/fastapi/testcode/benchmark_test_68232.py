# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import ast
from app_runtime import db


async def BenchmarkTest68232(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
