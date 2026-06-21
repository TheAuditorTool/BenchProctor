# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19371(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    int(str(data))
    return {"updated": True}
