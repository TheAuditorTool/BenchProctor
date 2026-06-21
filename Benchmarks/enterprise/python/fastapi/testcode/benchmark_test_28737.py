# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28737(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    eval(str(data))
    return {"updated": True}
