# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest01069(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = coalesce_blank(ua_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
