# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64


async def BenchmarkTest15289(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
