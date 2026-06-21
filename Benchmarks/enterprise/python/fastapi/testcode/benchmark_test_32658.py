# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32658(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
