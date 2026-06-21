# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest44150(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
