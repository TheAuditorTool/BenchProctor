# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07689(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    int(str(data))
    return {"updated": True}
