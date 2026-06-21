# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest40627(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
