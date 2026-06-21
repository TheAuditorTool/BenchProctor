# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16860(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
