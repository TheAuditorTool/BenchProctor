# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05507(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
