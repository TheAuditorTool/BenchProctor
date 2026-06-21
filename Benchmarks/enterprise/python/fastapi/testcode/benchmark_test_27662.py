# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27662(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
