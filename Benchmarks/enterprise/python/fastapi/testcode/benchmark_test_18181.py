# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18181(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
