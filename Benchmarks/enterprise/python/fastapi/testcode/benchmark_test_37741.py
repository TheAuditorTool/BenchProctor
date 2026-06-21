# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37741(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
