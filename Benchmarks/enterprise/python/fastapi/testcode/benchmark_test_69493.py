# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69493(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    eval(str(data))
    return {"updated": True}
