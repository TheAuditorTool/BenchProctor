# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest26316(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        os.setuid(int(str(referer_value)) if str(referer_value).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
