# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00650(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    eval(str(data))
    return {"updated": True}
