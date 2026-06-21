# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest69807(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
