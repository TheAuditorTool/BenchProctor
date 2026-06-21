# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44326(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
