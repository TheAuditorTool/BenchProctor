# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest50473(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
