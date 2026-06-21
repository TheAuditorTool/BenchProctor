# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest68241(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', raw_body):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = raw_body
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
