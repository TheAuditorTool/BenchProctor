# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest15953(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
