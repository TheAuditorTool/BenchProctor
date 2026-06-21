# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04632(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
