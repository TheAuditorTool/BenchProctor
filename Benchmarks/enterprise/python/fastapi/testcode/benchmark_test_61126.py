# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest61126(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    return JSONResponse({'error': str(raw_body), 'stack': repr(locals())}, status_code=500)
