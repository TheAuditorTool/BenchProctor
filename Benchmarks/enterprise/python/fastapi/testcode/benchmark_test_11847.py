# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11847(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
