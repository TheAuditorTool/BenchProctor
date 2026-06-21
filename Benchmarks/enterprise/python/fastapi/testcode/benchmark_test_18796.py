# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest18796(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    os.remove(str(data))
    return {"updated": True}
