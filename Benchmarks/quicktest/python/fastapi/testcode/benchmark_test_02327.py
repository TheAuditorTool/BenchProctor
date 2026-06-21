# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02327(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    exec(str(data))
    return {"updated": True}
