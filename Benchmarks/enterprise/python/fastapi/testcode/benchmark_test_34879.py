# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest34879(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
