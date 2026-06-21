# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import re
from fastapi import Form
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest22288(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    globals()['counter'] = int(processed)
    return {"updated": True}
