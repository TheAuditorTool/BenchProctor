# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23412(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    result = 100 / int(str(data))
    return {"updated": True}
