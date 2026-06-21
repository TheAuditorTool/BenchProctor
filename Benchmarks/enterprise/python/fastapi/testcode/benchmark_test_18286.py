# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18286(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    eval(str(data))
    return {"updated": True}
