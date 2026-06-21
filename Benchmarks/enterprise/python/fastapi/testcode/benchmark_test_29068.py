# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29068(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
