# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32921(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    eval(str(data))
    return {"updated": True}
