# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17098(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
