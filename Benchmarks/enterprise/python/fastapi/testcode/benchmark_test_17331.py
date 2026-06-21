# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest17331(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
