# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest20250(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    os.system('echo ' + str(data))
    return {"updated": True}
