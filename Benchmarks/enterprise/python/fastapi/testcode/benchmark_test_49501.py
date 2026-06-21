# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest49501(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    raise RuntimeError('processing failed: ' + str(cookie_value))
    return {"updated": True}
