# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62106(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    eval(str(data))
    return {"updated": True}
