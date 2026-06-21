# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32914(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    int(str(data))
    return {"updated": True}
