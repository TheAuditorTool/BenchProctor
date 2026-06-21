# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest01748(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JSONResponse({'action': action}, status_code=200)
