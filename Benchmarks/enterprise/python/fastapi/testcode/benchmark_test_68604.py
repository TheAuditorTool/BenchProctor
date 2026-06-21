# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68604(request: Request):
    auth_header = request.headers.get('authorization', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(auth_header))
    return {"updated": True}
