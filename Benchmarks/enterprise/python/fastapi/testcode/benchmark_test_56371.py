# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56371(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    int(str(data))
    return {"updated": True}
