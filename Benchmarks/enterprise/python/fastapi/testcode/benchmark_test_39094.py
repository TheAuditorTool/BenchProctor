# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39094(request: Request):
    origin_value = request.headers.get('origin', '')
    data = (lambda v: v.strip())(origin_value)
    result = 100 / int(str(data))
    return {"updated": True}
