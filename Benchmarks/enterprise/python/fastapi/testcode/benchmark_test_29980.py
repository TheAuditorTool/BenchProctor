# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


async def BenchmarkTest29980(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if re.search('[a-zA-Z0-9_-]+', str(raw_body)):
        return JSONResponse({'validated': str(raw_body)}, status_code=200)
    return {"updated": True}
