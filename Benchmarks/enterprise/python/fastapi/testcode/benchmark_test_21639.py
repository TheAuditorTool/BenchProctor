# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest21639(request: Request, field: str = Form('')):
    field_value = field
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', field_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = field_value
    eval(str(processed))
    return {"updated": True}
