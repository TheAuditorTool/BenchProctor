# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


async def BenchmarkTest03085(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
