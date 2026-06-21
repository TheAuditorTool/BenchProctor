# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43620(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
