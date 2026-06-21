# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21376(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    prefix = ''
    data = prefix + str(header_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
