# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39931(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    int(str(data))
    return {"updated": True}
