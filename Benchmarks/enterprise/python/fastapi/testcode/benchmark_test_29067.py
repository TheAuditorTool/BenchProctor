# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29067(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
