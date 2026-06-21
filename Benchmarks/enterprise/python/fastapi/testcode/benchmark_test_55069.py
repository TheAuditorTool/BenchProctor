# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55069(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    eval(str(data))
    return {"updated": True}
