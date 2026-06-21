# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29261(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
