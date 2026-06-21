# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41668(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
