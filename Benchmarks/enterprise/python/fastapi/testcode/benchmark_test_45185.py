# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45185(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    int(str(data))
    return {"updated": True}
