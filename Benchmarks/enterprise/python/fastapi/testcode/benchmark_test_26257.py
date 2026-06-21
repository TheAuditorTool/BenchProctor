# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest26257(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    os.remove(str(data))
    return {"updated": True}
