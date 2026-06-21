# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39360(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
