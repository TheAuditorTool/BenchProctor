# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58881(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
