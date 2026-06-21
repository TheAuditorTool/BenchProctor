# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


async def BenchmarkTest74762(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
