# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35983(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
