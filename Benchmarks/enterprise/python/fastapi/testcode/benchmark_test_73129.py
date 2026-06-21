# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


request_state: dict[str, str] = {}

async def BenchmarkTest73129(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
