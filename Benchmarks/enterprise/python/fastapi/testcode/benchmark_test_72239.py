# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72239(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % str(ua_value)
    int(str(data))
    return {"updated": True}
