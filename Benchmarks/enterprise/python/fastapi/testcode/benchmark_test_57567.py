# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


def ensure_str(value):
    return str(value)

async def BenchmarkTest57567(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
