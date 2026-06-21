# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest24237(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
