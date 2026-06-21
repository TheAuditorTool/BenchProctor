# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55846(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
