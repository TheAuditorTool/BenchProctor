# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest62634(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
