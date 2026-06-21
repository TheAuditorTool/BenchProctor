# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27206(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
