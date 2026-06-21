# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest52925(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    os.system('echo ' + str(data))
    return {"updated": True}
