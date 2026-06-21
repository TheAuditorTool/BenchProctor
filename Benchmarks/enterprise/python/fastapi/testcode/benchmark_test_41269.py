# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41269(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
