# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest56294(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    os.remove(str(data))
    return {"updated": True}
