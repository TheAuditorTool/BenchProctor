# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36234(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
