# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15508(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
