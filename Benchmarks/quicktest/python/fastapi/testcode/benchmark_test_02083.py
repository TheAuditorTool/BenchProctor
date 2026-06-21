# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest02083(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
