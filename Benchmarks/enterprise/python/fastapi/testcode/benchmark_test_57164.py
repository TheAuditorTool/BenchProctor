# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57164(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
