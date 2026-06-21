# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38596(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = (lambda v: v.strip())(auth_header)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
