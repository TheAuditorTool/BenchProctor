# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03998(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
