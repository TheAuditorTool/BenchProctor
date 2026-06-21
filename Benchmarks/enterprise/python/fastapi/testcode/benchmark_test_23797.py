# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23797(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
