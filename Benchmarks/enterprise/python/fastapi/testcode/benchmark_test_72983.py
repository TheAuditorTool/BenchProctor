# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72983(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    size = min(int(cookie_value) if str(cookie_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
