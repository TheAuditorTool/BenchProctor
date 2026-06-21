# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66448(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    eval(str(data))
    return {"updated": True}
