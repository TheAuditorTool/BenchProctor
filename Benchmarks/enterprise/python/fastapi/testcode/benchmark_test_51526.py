# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest51526(request: Request):
    referer_value = request.headers.get('referer', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', referer_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = referer_value
    eval(str(processed))
    return {"updated": True}
