# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04648(request: Request):
    path_value = request.path_params.get('id', '')
    size = min(int(path_value) if str(path_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
