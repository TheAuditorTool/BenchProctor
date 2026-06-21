# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36265(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
