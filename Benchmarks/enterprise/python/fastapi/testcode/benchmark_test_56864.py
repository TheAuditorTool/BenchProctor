# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56864(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '{}'.format(ua_value)
    eval(str(data))
    return {"updated": True}
