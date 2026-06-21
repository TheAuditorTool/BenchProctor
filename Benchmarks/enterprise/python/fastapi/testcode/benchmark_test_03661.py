# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03661(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
