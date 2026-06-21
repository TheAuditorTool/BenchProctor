# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73705(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ' '.join(str(auth_header).split())
    eval(str(data))
    return {"updated": True}
