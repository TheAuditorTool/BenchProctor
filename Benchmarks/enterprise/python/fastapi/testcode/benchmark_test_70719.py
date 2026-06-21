# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70719(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
