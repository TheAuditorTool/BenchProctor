# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest19896(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        os.setuid(int(str(auth_header)) if str(auth_header).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
