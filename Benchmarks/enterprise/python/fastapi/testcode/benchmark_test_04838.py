# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


async def BenchmarkTest04838(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
