# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest57210(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
