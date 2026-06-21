# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48282(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
