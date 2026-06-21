# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest65425(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
