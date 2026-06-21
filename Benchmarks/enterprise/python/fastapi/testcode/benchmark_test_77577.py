# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest77577(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
