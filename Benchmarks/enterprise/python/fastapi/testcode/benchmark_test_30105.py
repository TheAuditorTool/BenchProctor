# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def ensure_str(value):
    return str(value)

async def BenchmarkTest30105(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
