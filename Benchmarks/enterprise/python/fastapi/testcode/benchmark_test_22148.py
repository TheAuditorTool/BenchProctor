# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest22148(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(raw_body)})
