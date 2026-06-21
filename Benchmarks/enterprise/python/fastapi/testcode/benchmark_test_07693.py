# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07693(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    eval(str(data))
    return {"updated": True}
