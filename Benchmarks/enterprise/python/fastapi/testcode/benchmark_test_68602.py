# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68602(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
