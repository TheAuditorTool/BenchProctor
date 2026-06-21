# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest09373(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    int(str(data))
    return {"updated": True}
