# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest81347(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
