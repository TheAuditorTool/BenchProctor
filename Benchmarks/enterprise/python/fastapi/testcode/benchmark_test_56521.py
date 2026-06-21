# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56521(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
