# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28629(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
