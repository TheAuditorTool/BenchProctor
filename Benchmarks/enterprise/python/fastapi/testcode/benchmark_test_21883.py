# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest21883(request: Request, field: str = Form('')):
    field_value = field
    if field_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = field_value
    return HTMLResponse(str(processed))
