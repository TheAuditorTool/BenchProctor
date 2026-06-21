# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def to_text(value):
    return str(value).strip()

async def BenchmarkTest60128(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
