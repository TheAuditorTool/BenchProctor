# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59708(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
