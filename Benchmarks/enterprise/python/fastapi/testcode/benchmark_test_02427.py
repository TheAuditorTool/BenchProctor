# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest02427(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
