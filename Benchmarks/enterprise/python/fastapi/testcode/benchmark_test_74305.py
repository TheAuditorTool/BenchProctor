# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74305(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
