# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43035(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
