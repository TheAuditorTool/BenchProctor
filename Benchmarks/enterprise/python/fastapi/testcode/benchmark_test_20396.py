# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20396(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    int(str(data))
    return {"updated": True}
