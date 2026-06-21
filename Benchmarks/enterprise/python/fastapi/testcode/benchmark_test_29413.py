# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29413(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    with open('/var/app/data/' + str(cookie_value), 'r') as fh:
        content = fh.read()
    return content
