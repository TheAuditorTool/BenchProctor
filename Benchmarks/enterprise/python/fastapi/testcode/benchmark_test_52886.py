# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest52886(request: Request, field: str = Form('')):
    field_value = field
    parts = str(field_value).split(',')
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JSONResponse({'action': action}, status_code=200)
