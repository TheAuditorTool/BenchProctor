# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78434(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = str(ua_value).replace('\x00', '')
    eval(str(data))
    return {"updated": True}
