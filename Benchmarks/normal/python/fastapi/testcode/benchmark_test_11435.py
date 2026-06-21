# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11435(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    exec(str(data))
    return {"updated": True}
