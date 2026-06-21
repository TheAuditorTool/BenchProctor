# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32379(request: Request):
    ua_value = request.headers.get('user-agent', '')
    with open('/var/app/data/' + str(ua_value), 'r') as fh:
        content = fh.read()
    return content
