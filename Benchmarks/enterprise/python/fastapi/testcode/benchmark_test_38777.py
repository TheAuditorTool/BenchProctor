# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38777(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    eval(str(data))
    return {"updated": True}
