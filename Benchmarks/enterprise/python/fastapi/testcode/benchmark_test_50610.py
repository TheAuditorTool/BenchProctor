# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest50610(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
