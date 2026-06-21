# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14965(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    eval(str(cookie_value))
    return {"updated": True}
