# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest75608(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    os.system('echo ' + str(data))
    return {"updated": True}
