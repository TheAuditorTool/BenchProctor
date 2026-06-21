# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest80864(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    int(str(data))
    return {"updated": True}
