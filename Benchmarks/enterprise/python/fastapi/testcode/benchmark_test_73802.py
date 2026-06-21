# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest73802(request: Request, field: str = Form('')):
    field_value = field
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
