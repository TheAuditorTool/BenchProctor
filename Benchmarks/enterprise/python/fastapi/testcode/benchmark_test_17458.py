# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17458(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
