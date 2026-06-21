# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04031(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
