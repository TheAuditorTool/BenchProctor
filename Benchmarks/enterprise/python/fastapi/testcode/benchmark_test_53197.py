# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53197(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    eval(str(data))
    return {"updated": True}
