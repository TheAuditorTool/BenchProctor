# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest78788(request: Request):
    referer_value = request.headers.get('referer', '')
    data = to_text(referer_value)
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
