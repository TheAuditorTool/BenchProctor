# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest22139(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = default_blank(ua_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
