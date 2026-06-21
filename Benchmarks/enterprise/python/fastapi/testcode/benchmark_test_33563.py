# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33563(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    result = 100 / int(str(data))
    return {"updated": True}
