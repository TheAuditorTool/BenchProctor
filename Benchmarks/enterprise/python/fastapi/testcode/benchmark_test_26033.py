# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26033(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
