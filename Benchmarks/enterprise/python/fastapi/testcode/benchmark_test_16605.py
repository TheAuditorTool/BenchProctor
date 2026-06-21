# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16605(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
