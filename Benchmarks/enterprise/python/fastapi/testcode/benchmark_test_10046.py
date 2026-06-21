# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import base64


async def BenchmarkTest10046(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
