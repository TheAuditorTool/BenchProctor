# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12334(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % str(origin_value)
    result = 100 / int(str(data))
    return {"updated": True}
