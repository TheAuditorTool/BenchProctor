# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28205(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
