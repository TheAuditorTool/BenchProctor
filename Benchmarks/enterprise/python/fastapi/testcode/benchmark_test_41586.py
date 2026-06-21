# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest41586(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', ua_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = ua_value
    eval(str(processed))
    return {"updated": True}
