# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest74916(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JSONResponse({'action': action}, status_code=200)
