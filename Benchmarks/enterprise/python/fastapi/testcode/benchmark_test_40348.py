# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


async def BenchmarkTest40348(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
