# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23233(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
