# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16317(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
