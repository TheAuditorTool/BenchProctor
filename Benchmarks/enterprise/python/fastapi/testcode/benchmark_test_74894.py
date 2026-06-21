# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74894(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
