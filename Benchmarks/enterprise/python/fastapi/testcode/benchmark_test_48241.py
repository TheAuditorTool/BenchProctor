# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48241(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    result = 100 / int(str(data))
    return {"updated": True}
