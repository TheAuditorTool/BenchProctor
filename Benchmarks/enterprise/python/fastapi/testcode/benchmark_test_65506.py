# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest65506(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
