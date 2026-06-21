# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56769(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
