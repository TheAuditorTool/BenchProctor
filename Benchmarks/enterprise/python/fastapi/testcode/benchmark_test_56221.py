# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56221(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
