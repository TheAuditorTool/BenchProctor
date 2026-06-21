# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58346(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '{}'.format(ua_value)
    int(str(data))
    return {"updated": True}
