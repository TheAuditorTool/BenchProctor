# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08854(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
