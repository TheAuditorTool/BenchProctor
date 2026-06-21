# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21521(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
