# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest32671(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    os.system('echo ' + str(data))
    return {"updated": True}
