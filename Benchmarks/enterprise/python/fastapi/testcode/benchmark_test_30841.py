# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest30841(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
