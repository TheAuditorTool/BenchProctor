# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79085(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
