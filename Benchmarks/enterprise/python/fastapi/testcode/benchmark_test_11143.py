# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11143(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
