# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28668(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
