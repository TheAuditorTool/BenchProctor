# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78651(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
