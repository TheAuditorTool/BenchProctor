# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest59841(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = xml_value
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
