# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09851(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    result = 100 / int(str(data))
    return {"updated": True}
