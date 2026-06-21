# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10632(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    int(str(data))
    return {"updated": True}
