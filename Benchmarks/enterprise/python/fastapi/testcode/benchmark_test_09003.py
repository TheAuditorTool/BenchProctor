# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest09003(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    os.remove(str(data))
    return {"updated": True}
