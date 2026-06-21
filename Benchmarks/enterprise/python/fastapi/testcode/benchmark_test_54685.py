# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest54685(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    eval(str(data))
    return {"updated": True}
