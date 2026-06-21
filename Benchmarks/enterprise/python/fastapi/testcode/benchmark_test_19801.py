# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19801(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    request.session['data'] = str(data)
    return {"updated": True}
