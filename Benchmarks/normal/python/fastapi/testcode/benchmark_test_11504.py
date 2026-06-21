# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest11504(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
