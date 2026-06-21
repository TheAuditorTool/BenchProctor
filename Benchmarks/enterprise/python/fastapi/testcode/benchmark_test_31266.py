# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31266(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    request.session['data'] = str(data)
    return {"updated": True}
