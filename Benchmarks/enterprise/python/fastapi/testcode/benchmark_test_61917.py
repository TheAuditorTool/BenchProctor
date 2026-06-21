# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61917(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
