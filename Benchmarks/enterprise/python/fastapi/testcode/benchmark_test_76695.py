# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76695(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    request.session['data'] = str(data)
    return {"updated": True}
