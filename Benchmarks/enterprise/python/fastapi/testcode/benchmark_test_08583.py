# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08583(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    int(str(data))
    return {"updated": True}
