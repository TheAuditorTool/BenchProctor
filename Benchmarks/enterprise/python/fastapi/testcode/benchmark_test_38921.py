# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38921(request: Request):
    referer_value = request.headers.get('referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
