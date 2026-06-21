# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31921(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
