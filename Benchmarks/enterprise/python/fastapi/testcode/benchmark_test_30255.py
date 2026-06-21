# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30255(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
