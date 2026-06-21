# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest07438(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = raw_body
    eval(str(processed))
    return {"updated": True}
