# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18728(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
