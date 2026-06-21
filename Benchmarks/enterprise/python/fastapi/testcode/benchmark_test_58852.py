# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest58852(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
