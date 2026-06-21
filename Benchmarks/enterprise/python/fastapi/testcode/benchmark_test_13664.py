# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13664(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    request.session['user'] = str(data)
    return {"updated": True}
