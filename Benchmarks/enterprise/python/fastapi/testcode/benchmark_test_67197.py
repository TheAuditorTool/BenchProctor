# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


def ensure_str(value):
    return str(value)

async def BenchmarkTest67197(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ensure_str(raw_body)
    if time.time() > 1000000000:
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
