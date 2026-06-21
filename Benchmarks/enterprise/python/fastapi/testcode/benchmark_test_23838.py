# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23838(request: Request):
    origin_value = request.headers.get('origin', '')
    result = 100 / int(str(origin_value))
    return {"updated": True}
