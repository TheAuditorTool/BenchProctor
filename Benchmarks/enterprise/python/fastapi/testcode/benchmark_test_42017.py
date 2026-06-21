# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42017(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
