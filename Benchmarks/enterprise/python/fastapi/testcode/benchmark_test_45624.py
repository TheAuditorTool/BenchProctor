# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45624(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
