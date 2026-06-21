# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest71474(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
