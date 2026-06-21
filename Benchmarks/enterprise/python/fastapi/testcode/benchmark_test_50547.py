# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50547(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    eval(str(data))
    return {"updated": True}
