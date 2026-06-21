# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03754(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
