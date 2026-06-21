# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03482(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
