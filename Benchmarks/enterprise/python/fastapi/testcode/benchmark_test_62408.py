# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest62408(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
