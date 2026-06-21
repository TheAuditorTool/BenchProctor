# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28628(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    int(str(data))
    return {"updated": True}
