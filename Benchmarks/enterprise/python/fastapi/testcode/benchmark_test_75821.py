# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest75821(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    exec(str(data))
    return {"updated": True}
