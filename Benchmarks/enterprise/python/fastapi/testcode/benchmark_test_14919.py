# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest14919(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
