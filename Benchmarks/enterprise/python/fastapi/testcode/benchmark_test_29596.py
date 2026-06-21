# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29596(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    eval(str(data))
    return {"updated": True}
