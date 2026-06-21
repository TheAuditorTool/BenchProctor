# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02613(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    eval(str(data))
    return {"updated": True}
