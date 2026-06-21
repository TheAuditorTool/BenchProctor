# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest70376(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    os.remove(str(data))
    return {"updated": True}
