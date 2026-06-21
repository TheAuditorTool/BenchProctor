# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76025(request: Request):
    host_value = request.headers.get('host', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(host_value))
    return {"updated": True}
