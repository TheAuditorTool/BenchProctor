# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest25131(request: Request):
    origin_value = request.headers.get('origin', '')
    eval(str(origin_value))
    return {"updated": True}
