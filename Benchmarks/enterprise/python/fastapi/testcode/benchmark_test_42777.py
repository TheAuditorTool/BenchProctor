# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest42777(request: Request):
    path_value = request.path_params.get('id', '')
    os.remove(str(path_value))
    return {"updated": True}
