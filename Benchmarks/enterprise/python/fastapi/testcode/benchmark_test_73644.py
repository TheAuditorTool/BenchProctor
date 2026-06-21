# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73644(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
