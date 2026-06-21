# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest58010(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
