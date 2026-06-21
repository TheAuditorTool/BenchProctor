# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest52450(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    int(str(data))
    return {"updated": True}
