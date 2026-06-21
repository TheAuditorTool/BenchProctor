# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33035(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
