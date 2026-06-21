# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32158(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
