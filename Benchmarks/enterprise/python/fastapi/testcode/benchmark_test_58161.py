# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58161(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    eval(str(data))
    return {"updated": True}
