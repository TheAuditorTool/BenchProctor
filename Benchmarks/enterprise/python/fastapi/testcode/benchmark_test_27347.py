# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27347(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
