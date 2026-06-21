# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62819(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
