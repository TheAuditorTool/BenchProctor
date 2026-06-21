# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53818(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
