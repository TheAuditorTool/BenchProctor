# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31550(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
