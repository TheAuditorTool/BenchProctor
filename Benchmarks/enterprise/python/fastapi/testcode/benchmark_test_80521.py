# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest80521(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return {"updated": True}
