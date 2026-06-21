# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44419(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
