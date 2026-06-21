# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08765(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    exec(str(data))
    return {"updated": True}
