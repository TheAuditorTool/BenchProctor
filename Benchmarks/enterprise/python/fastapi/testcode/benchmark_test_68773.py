# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68773(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    os.remove(str(data))
    return {"updated": True}
