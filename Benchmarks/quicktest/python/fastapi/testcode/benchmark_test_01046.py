# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote


async def BenchmarkTest01046(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    os.system('echo ' + str(data))
    return {"updated": True}
