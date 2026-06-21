# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08752(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    eval(str(data))
    return {"updated": True}
