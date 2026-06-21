# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36558(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
