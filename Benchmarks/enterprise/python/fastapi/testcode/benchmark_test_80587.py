# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80587(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
