# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest74355(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    os.remove(str(data))
    return {"updated": True}
