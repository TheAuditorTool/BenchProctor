# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63887(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
