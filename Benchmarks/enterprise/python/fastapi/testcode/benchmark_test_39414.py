# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39414(request: Request):
    ua_value = request.headers.get('user-agent', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(ua_value))
    return {"updated": True}
