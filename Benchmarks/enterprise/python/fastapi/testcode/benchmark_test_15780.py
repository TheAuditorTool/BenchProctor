# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest15780(request: Request, field: str = Form('')):
    field_value = field
    return JSONResponse({'error': str(field_value), 'stack': repr(locals())}, status_code=500)
