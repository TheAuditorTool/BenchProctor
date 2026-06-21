# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest52135(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
