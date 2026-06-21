# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01683(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
