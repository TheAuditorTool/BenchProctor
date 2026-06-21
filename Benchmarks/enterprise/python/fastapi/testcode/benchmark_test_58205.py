# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58205(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
