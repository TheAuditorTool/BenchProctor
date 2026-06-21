# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41819(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
