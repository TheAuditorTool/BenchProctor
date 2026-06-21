# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28210(request: Request):
    referer_value = request.headers.get('referer', '')
    data = (lambda v: v.strip())(referer_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
