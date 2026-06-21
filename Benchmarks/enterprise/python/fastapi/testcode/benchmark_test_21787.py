# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21787(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
