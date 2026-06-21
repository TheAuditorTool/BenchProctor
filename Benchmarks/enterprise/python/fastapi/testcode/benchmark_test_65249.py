# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest65249(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    int(str(data))
    return {"updated": True}
