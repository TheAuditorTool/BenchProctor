# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


async def BenchmarkTest02001(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
