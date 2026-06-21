# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest60268(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
