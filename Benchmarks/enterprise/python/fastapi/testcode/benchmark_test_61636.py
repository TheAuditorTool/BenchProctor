# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61636(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
