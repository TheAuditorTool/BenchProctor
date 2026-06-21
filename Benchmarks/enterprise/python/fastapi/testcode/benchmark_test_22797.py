# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest22797(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return {"updated": True}
