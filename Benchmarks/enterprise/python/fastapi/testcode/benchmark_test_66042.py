# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66042(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
