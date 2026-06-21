# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70083(request: Request):
    origin_value = request.headers.get('origin', '')
    data = str(origin_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
