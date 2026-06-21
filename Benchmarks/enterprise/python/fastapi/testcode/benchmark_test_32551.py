# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32551(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
