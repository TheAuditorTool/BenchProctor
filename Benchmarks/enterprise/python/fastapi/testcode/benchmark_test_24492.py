# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import ast


async def BenchmarkTest24492(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    request.session['user'] = str(data)
    return {"updated": True}
