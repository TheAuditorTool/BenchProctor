# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest63992(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
