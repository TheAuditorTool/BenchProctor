# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64310(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
