# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest25404(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
