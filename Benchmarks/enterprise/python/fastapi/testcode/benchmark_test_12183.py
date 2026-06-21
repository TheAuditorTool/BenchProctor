# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12183(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % str(ua_value)
    exec(str(data))
    return {"updated": True}
