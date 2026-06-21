# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34461(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
