# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest75885(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
