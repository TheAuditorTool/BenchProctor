# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29016(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % (ua_value,)
    eval(str(data))
    return {"updated": True}
