# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest29176(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    os.system('echo ' + str(data))
    return {"updated": True}
