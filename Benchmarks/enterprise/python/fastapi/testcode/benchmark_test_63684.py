# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63684(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
