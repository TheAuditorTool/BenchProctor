# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02202(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % str(forwarded_ip)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
