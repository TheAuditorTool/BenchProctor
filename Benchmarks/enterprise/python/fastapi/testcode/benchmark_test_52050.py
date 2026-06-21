# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest52050(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
