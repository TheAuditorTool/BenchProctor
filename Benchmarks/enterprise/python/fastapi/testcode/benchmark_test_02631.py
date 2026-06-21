# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02631(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = cookie_value
            data = parsed
        case _:
            data = cookie_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
