# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest46627(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
